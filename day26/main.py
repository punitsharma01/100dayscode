import pandas
student_dict = {
    "student": ["Punit", "Rohan", "Raju"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student, row.score)
    # print(row) comes as series so we can access using . column
    #Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_codes_df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_codes_dict = {row.letter: row.code for (index, row) in phonetic_codes_df.iterrows()}
# print(phonetic_codes_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_code():
    input_name = input("Please enter your name: ").upper()
    try:
        if len(input_name) > 0:
            phonetic_names = [phonetic_codes_dict[letter] for letter in input_name]
            phonetic_letter_name = {letter: phonetic_codes_dict[letter] for letter in input_name}
        else:
            raise ValueError
    except KeyError:
        print("Sorry! only letters allowed! Try Again ")
        generate_code()
    except ValueError:
        print("Sorry! Empty name not allowed! Try Again ")
        generate_code()
    else:
        print(phonetic_names)
        print(phonetic_letter_name)


generate_code()
# phonetic_name = {letter: code for (letter, code) in phonetic_codes_dict.items() if letter in input_name}
# print(phonetic_name)
