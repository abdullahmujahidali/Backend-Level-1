import ast  # helps us to process trees of Python abstract syntax grammar

file = open("Files/birthday.txt", "r")
data = file.read()
# ast.literal_eval Safely evaluate a string of Python literals.
birthday = ast.literal_eval(data)
file.close()
print("Welcome to the birthday dictionary. We know the birthdays of: ")

for key in birthday:
    print(key)

search = input("Who's birthday do you want to look up? \n")
if search in birthday:
    result = birthday[search]
else:
    None
if result is None:
    print('No Data')
else:
    print("{}'s birthday is {}".format(search, birthday[search]))
