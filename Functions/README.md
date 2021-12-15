# PART 1 - FUNCTIONS
This README file contains function based questions which are solved using Python language.

### Question No 1:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

### Answer No 1:

```python
def fibonacci_series(size):
    """Returns fibonacci series of an upper limit.
        LRU (Least Recently Used) cache discards last recently used item first.
            It organizes item in order of use for efficiency improvement.
    """
    if size == 0:
        return 0
    if size == 1 or size == 2:
        return 1
    if size > 2:
        return fibonacci_series(size-1) + fibonacci_series(size-2)
```

### Question No 2:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  What is the difference between a parameter and an argument?

### Answer No 2:
<b>Argument</b>:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; In general when we want to pass information to a function we use arguments, and we can pass them using the parameters of a function. We can add any number of arguments to the function separating them with comma. 

An example of an argument can be demonstrated using the example below:

```python
def sum(number1, number2):
    return number1 + number2
num1 = 2
num2 = 3
print(sum(num1, num2)) # Here num1 and num2 are the arguments that are being passed to the function.
```
There are 3 main types of arguments:

1. Default arguments: <br/>
  &nbsp; &nbsp; &nbsp;  A default argument are just constant values that are being passed to the function. An example of default argument is:
```python
        def sum(number1, number2=55, number2=32):
            return number1 + number2
        sum(2) # default argument example 2 and 3 are default arguments 
```


2. Keyword arguments: <br/>
  &nbsp; &nbsp; &nbsp;  Keyword arguments are arguments values that are needed to be passed with a key which refers to that value using keyword arguments we don't have to follow the order of parameters 
```python
        def sum(number1, number2):
            print("Number 1: ", number1)
            print("Number 2: ", number2)
            return number1 + number2
        sum(number2=4,number1=3) # keyword argument passed (value with a key) without following order sequence
```

3. Positional arguments: <br />
&nbsp; &nbsp; &nbsp;  A positional argument are arguments that are passed by following the arguments position. Positional arguments can be a mixture of default and keyword arguments too. 
```python
        def sum(number1, number2, number3):
            return number1 + number2
        sum(11,number3=2,number2=3) # combination of default and keyword argument.
        sum(number1=25,number3=2,number2=3) # positional argument
```

<b>Parameter</b>:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; In general when we want to our function to receive something we use parameters. If a function has some arguments than we are sure that our function will have some variables in the function signature and that is our parameters.

An example of an argument can be demonstrated using the example below:

```python
def sum(number1, number2): # Here number1 and number2 are the parameters that are received by our function.
    return number1 + number2
num1 = 2
num2 = 3
print(sum(num1, num2))
```
