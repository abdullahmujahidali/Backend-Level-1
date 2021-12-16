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

### Question No 2:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  Modify your program from Question 1 of this section to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program. Finally, ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

### Answer No 2:
``` python
import json
def write_json(data, filename='Files/birthday.json'):
    with open(filename, 'r+') as file:
        birthday = json.load(file)
        birthday["birthday"].update(data)
        file.seek(0)
        json.dump(birthday, file, indent=4)
        file.close()


def read_file():
    with open('Files/birthday.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    print("\n------------------------")
    for key in data['birthday']:
        print(key)
    print("------------------------\n")


read_file()
print("Add new scientist name and birthday into the file")
name = input("Enter new name of scientist: ")
birthday = input("Enter Date of Birth (format: DD/MM/YYYY): ")
obj = {name: birthday, }

write_json(obj)
```

### Question No 3:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  We saved information about famous scientists’ names and birthdays to disk. Now we load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month. (Hint: Use counter from the collections module.) Your program should output something like: 
```python
    {"May": 3,"November": 2,"December": 1}
```
### Answer No 3:

```python
import json

def read_file():
    with open('Files/birthday.json') as json_file:
        data = json.load(json_file)
        json_file.close()

    return data['birthday']


month = {
    "January": 0, "February": 0, "March": 0, "April": 0,
    "May": 0, "June": 0, "July": 0, "August": 0, "September": 0,
    "October": 0, "November": 0, "December": 0
}
monthInteger = {
    "01": "January", "02": 'February', "03": 'March', "04": 'April',
    "05": 'May', "06": 'June', "07": 'July', "08": 'August',
    "09": 'September', "10": 'October', "11": 'November', "12": 'December'
}
result = read_file()
value_list = []
for (key, values) in result.items():
    value_list.append(values[0:2])

for val in value_list:
    if val in monthInteger:
        month[monthInteger[val]] += 1
print(month)

```


### Question No 4:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  You have a list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

### Answer No 4:
```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = [num for num in a if num % 2 == 0]
print(new_list)

```
<b>EXPLANATION</b>:
Explanation of the above code is just another solution of the below code:
```python
new_list = []
for num in a:
    if num % 2 == 0:
        new_list.append(num)
print(new_list)

```
