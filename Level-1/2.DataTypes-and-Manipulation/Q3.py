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
