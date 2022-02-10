
dictionary = dict()
user_list = [
    ("kainat", "kainat", 15),
    ("abdullah", "abdullahmujahidali1@gmail.com", 23),
    ("maheen", "maheenali@", 23),
    ("maha", "mahaqureshi.com", 22),
    ("amna", "@amna.com", 27),
    ("lubna", "lubna@gmail.com", -13),
]


class DuplicateUserName(Exception):
    NotImplementedError()


class AgeNotValid(Exception):
    NotImplementedError()


class UserUnderAge(Exception):
    NotImplementedError()


class EmailNotValid(Exception):
    NotImplementedError()


class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


for index, tuple in enumerate(user_list):
    username = tuple[0]
    email = tuple[1]
    age = tuple[2]
    email_split = email.split('@')
    print("EMAIL: ", email_split)
    try:
        if len(email_split) != 2 or not email_split[0] or not email_split[1]:
            raise EmailNotValid()
        if username in dictionary:
            raise DuplicateUserName
        if age < 0:
            raise AgeNotValid
        if age < 16:
            raise UserUnderAge
    except DuplicateUserName:
        print("Username {} is in use.".format(username))
    except AgeNotValid:
        print("{} age is: {} which is invalid".format(username, age))
    except UserUnderAge:
        print("{} is underage.".format(username))
    except EmailNotValid:
        print("Email: {} is not a valid".format(email))
    else:
        dictionary[username] = User(username, email, age)
