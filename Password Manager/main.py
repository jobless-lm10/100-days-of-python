from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- SEARCH EXISTING DETAILS ------------------------------- #
def search_details():
    website = website_entry.get()
    try:
        with open("C:/Users/rig/Desktop/Videos/Passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # print("No Records Found")
        messagebox.showerror(title="Error Occurred", message="No Records Found")
    else:
        try:
            website_details = data[website]
        except KeyError:
            messagebox.showerror(title="Error Occurred", message=f"{website} details not found.")
        else:
            # password_entry.insert(0, website_details["password"])
            # username_entry.insert(0, website_details["email"])
            messagebox.showinfo(title="Website Details", message=f"Email/Username: {website_details['email']}\n"
                                                                 f"Password: {website_details['password']}")
            pyperclip.copy(website_details["password"])


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    new_data_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Missing Fields", message="Some input fields are empty")

    # Using Text file to store details
    # elif messagebox.askokcancel(title=website, message=f"Email/Username: {email}\nPassword: {password}\n"
    #                                                    f"Want to proceed with saving details?"):
    #     with open("Passwords.txt", "a") as data_file:
    #         data_file.write(f"{website} | {email} | {password}\n")

    else:
        try:
            with open("C:/Users/rig/Desktop/Videos/Passwords.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data_dict)

        except FileNotFoundError:
            with open("C:/Users/rig/Desktop/Videos/Passwords.json", "w") as data_file:
                json.dump(new_data_dict, data_file, indent=4)

        else:
            with open("C:/Users/rig/Desktop/Videos/Passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", bg=YELLOW, font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)
website_label = Label(text="Email/Username: ", bg=YELLOW, font=(FONT_NAME, 12))
website_label.grid(column=0, row=2)
website_label = Label(text="Password: ", bg=YELLOW, font=(FONT_NAME, 12))
website_label.grid(column=0, row=3)

website_entry = Entry(width=26)
website_entry.grid(column=1, row=1)
website_entry.focus()
username_entry = Entry(width=44)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "adityasingh770@protonmail.com")
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search_details)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(width=36, text="Add", command=save_details)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
