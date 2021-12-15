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

### Question No 3:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  All functions in Python by default return …?

### Answer No 3:
Yes Python does return something default if a function that doesn't return anything it means that it is returning None which is itself a value. We all know that each function with a returning value return something but what about a non-returning function? Below is the demonstration to support the answer that it does return something.

```python
def non_returning_function():
  pass

print("Function returned: ", non_returning_function())
```
Output:
# ![alt text](https://i.ibb.co/GP8mrqS/Screenshot-2021-12-15-at-3-14-27-PM.png "Logo Title") 

The output above shows that even a function that looks like it isn't returning anything visually but it does return None.


### Question No 4:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  What are keyword arguments and when should we use them?
### Answer No 4:
Keyword arguments: <br/>
  &nbsp; &nbsp; &nbsp;  Keyword arguments are arguments values that are needed to be passed with a key which refers to that value using keyword arguments we don't have to follow the order of parameters 
```python
        def sum(number1, number2):
            print("Number 1: ", number1)
            print("Number 2: ", number2)
            return number1 + number2
        sum(number2=4,number1=3) # keyword argument passed (value with a key) without following order sequence
```

We can use keyword arguments when we want to pass only a few number of arguments and don't want to pass argument for default values so in that case keyword arguments are used and when we are trying to return a number of values we use keyword argument to make it more readable for us that which values belongs to which argument.


### Question No 5:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  How can we make a parameter of a function optional?
### Answer No 5:

