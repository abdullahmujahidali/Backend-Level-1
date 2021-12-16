# ![alt text](https://carteblanche.tech/static/static/website/images/general/logo.svg "Logo Title")  &nbsp; &nbsp;  PART 2 - DATA TYPES & MANIPULATION

This README file contains data types and manipulations based questions which are solved using Python language.

### Question No 1:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; We will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name and return the birthday of that person back to them. The interaction should look something like this:
```
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
```

### Answer No 1:
``` python
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
```