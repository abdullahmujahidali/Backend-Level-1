# ![Logo](https://carteblanche.tech/static/static/website/images/general/logo.svg "Logo Title")  &nbsp; &nbsp;  PART 3 - CONTROL FLOW

This README file contains control flow based questions which are solved using Python language.

### Question No 1:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What is the difference between 10 / 3 and 10 // 3?

### Answer No 1:
`10/3` is float division if we want float division of numbers we will use single division operator `/` and for integer division we use `//`. So `10 // 3` is will give us integer value result.

The result of `10/3` will be `3.3333`.

The result of `10//3` will be `3`.


### Question No 2:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  What is the result of 10 ** 3?

### Answer No 2:
The result of ` 10 ** 3` is 1000. As ** operator in terms of mathematical computation means power operator where the value before operator is the base and the value after the operator is the power of that base. So here the piece of code means 10 power 3 which is 1000.

### Question No 3:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Given (x = 1), what will be the value of after we run (x += 2)?

### Answer No 3:
The result of `(x +=2) ` when `(x=1)` will be 3. It is because we are pre-incrementing the value of x with 2. Previously we initialized the value of x with 1. So after pre-incrementing the value when we print the new value of x we get <b> 3 </b> as answer.

### Question No 4:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; How can we round a number?

### Answer No 4:
We use Python built-in function `round()` to round a number. If we don't pass any parameter to our round function we will get a whole number because the default is 0. The other case if we pass an integer value as a 2nd parameter we will get that number of decimal places answer as a result.
```python
print(round(3.23))
# OUTPUT: 3

print(round(3.23, 1))
# OUTPUT: 3.2

```


### Question No 5:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What is the result of float(1)?

### Answer No 5:
The result of the above expression will output 1.0. If we pass no argument inside the float function it will give us 0.0 as an answer.
Float is a typecast function for data types for example. integer and string.
```python
print(float(1))
# OUTPUT 1.0

print(float('2'))
# OUTPUT 2.0
```

### Question No 6:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What is the result of bool(“False”)?

### Answer No 6:
The result of the above expression will output True. If we pass no argument inside the bool function it will give us False as an answer.
Bool is a typecast function for data types. If nothing False or 0(except for string) is passed it will return False and for every other case it will return True
```python
print(bool(1))
# OUTPUT True

print(bool())
# OUTPUT False

print(bool(False))
# OUTPUT False
```

### Question No 7:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What are the falsy values in Python?

### Answer No 7:
All those values that are None, 0, empty, False are the falsy values in Python. For instance ```python [],(),{}," ",0,0.0,0j, None , False ``` are the falsy values that are in Python.

### Question No 8:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What is the result of 10 == “10”?
### Answer No 8:
The answer to the above expression is False because the both have different data types, one is an integer and the other one is a string so they are not equal and that's why we get False as answer. 

### Question No 9:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; What is the result of “bag” > “apple”?

### Answer No 9:
The answer to the expression `“bag” > “apple”` will return `True` because of the ordering the word as characters are converted into UNICODE and after converting into UNICODE they are being evaluated based on their UNICODE value. The order of bag is greater than apple so that's why it returned `True`.

### Question No 10:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  What is the result of not(True or False)?

### Answer No 10:
The answer of the expression `not(True or False)` will return us False and that's because of the not operator (True or False) will return us True (0 or 1 = True) but after that the not operator reverse the answer so in the end we get `False` as output.

### Question No 11:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Under what circumstances does the expression 18 <= age < 65 evaluate to True?

### Answer No 11:
The expression will return True for cases when age is greater equal to 18 and lesser than 65. So it means any number from 18-64 inclusive will return True. Other cases beside the mentioned will always return False.

### Question No 12:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  What does range(1, 10, 2) return?

### Answer No 12:
Range function has a total of 3 parameters.

1. Start of Range (1 is the start of the range from the question)
2. End of Range (10 is the end of the range from the question)
3. Incremental value (2 is the incremental value of the range from the question)

So the above range function will return values from 1 to 10 with an increment of 2. If we look at the below code we can understand it better.
```python
for i in  range(1, 10, 2) :
  print(i, end=",") 
# OUTPUT: 1,3,5,7,9
```
So in each iteration +2 is added to the current value of i until we reach the end of the range.

### Question No 13:
#### &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Name 3 iterable objects in Python.

### Answer No 13:
An iterable object in Python are iterable objects that can be iterated through a loop returning one value at a time. The three most used iterable objects in Python are: Lists, Dictionary and Tuples.

