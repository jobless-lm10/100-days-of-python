import pandas

# TODO 1. Create a dictionary in this format:
phonetics_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter:row.code for (index, row) in phonetics_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word to convert into its NATO phonetic equivalent: ")
result_list = [phonetics_dict[letter.upper()] for letter in user_input]
print(result_list)
