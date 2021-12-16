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
