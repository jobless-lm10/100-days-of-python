# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names_str = names_file.read()

names_list = names_str.strip().split("\n")

for name in names_list:
    with open(f"./Output/{name}.txt", "w") as output:
        output.write(letter.replace("[name]", name))
