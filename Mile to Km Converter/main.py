import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40)


def on_calculate():
    miles = input_miles.get()
    km_value.config(text=f"{float(miles) * 1.61:.2f}")


equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1, padx=5, pady=5)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0, padx=5, pady=5)

mile_label = tkinter.Label(text="Miles", font=("Arial", 12))
mile_label.grid(column=2, row=0, padx=5, pady=5)

km_value = tkinter.Label(text="0", font=("Arial", 12))
km_value.grid(column=1, row=1, padx=5, pady=5)

km_label = tkinter.Label(text="Kms", font=("Arial", 12))
km_label.grid(column=2, row=1, padx=5, pady=5)

calculate_button = tkinter.Button(text="Calculate", font=("Arial", 12), command=on_calculate)
calculate_button.grid(column=1, row=2, padx=5, pady=5)

window.mainloop()
