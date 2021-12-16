import json  # helps us to process trees of Python abstract syntax grammar

with open('Files/birthday.json') as json_file:
    data = json.load(json_file)
    print("Data:", (data))

    dict = Dictionary()
# student = json.loads(data)
# if "Albert Einstein" in student:
#     print("Key exist in JSON data")
#     print(student["14/3/1889"], "marks is: ", student["Albert Einstein"])
# else:
#     print("Key doesn't exist in JSON data")
# keyVal = input("Enter a key value: \n")
# if keyVal in data:
#     # Print the success message and the value of the key
#     print("%s is found in JSON data" %keyVal)
#     print("The value of", keyVal,"is", data[keyVal])
# else:
#     # Print the message if the value does not exist
#     print("%s is not found in JSON data" %keyVal)

#     print("\nPeople1:", data['people1'])
#     print("\nPeople2:", data['people2'])

# file = open("Files/birthday.json", "r")
# data = json.load(file)
# # ast.literal_eval Safely evaluate a string of Python literals.
# for i in data['birthday']:
#     print(i)
# file.close()
# print("Welcome to the birthday dictionary. We know the birthdays of: ")
# print(birthday)

# for key in birthday:
#     print(key)

# search = input("Who's birthday do you want to look up? \n")
# if search in birthday:
#     result = birthday[search]
# else:
#     None
# if result is None:
#     print('No Data')
# else:
#     print("{}'s birthday is {}".format(search, birthday[search]))
