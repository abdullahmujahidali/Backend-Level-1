# ![alt text](https://carteblanche.tech/static/static/website/images/general/logo.svg "Logo Title")  &nbsp; &nbsp;  PART 4 - OBJECT ORIENTED PROGRAMMING (OOP)

This README file contains OOP (Object Oriented Programming) based questions which are solved using Python language.

### Question No 1:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1. A very common use case for inheritance is the creation of a custom exception hierarchy. Because we use the class of an exception to determine whether it should be caught by a particular except block, it is useful for us to define custom classes for exceptions which we want to raise in our code. Using inheritance in our classes is useful because if an except block catches a particular exception class, it will also catch its child classes (because a child class is its parent class). That means that we can efficiently write except blocks which handle groups of related exceptions, just by arranging them in a logical hierarchy. Our exception classes should inherit from Python’s built-in exception classes. They often won’t need to contain any additional attributes or methods.
* Write a simple program which loops over a list of user data (tuples containing a username, email and age) and adds each user to a directory if the user is at least 16 years old. You do not need to store the age. Write a simple exception hierarchy which defines a different exception for each of these error conditions:
    1. the username is not unique
    2. the age is not a positive integer
    3. the user is under 16
    4. the email address is not valid (a simple check for a username, the @ symbol and a domain name is sufficient)
* Raise these exceptions in your program where appropriate. Whenever an exception occurs, your program should move onto the next set of data in the list. Print a different error message for each different kind of exception.
* Think about where else it would be a good idea to use a custom class, and what kind of collection type would be most appropriate for your directory.
* You can consider an email address to be valid if it contains one @ symbol and has a non-empty username and domain name – you don’t need to check for valid characters. You can assume that the age is already an integer value.

### Sub Questions:

1. Write an “abstract” class, Box, and use it to define some methods which any box object should have: add, for adding any number of items to the box, empty, for taking all the items out of the box and returning them as a list, and count, for counting the items which are currently in the box. Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
2. Extending question 2 of this section, Write a function, repack_boxes, which takes any number of boxes as parameters, gathers up all the items they contain, and redistributes them as evenly as possible over all the boxes. Order is unimportant. There are multiple ways of doing this. Test your code with a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. You should end up with two boxes with 11 items each, and one box with 12 items.


### Answer:
