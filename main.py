student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv").to_dict()
nato_dict = { data["letter"][i] : data["code"][i] for i in data["letter"] }


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


while True:
    user = input("Hello what is your name? ").upper()
    try:
        new_user = [nato_dict[x] for x in user]

    except KeyError:
        print("That's not a letter. Try again.")
    else:
        break


final_list = []

        
print(new_user)