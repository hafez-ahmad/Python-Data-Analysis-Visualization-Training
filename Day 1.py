
# # 1. Python Fundamentals (Day 1)
# [All code will be shared in the github page](https://github.com/hafez-ahmad/Python-Data-Analysis-Visualization-Training)
# 
# If you have questions, Please ask or post in the github issue
# 

# %% [markdown]
# # 1.1  Setup Python
# 
# 
# 
# ## (a) Install from [Anaconda Distribution](https://www.anaconda.com/download) <br >
# ## (b) Open anaconda prompt /terminal
# 
# <br>
# 
# ![Alt text](image-2.png)
# 
# <br> Jupyter notebook   --> run code (Ctrl + Enter) or (Alt+Enter)
# 
# ![Alt text](image-3.png)
# 

# %% [markdown]
# # 1.2 Basic Python syntax and data types
# | Syntax                 | Description                                       |
# |------------------------|---------------------------------------------------|
# | `print("Hello, World!")` | Print the string "Hello, World!"                  |
# | `# This is a comment`   | Single-line comment                               |
# | `"""Multiline string"""` | Multiline string (used for documentation)         |
# | `x = 5`                | Assign the value 5 to variable x                  |
# | `if/for/while condition:`        | Conditional statement                             |
# | `import module`        | Import a Python module                           |
# | `from module import x` | Import specific variable/function from a module  |
# 
# # Data type
# 
# | Data Type       | Description                   | Example                  |
# |-----------------|-------------------------------|--------------------------|
# | int             | Integer (whole number)        | `42`                     |
# | float           | Floating-point (decimal)      | `3.14`                   |
# | str             | String (text)                 | `'Hello, World!'`        |
# | bool            | Boolean (True/False)          | `True` or `False`        |
# | list            | List (ordered collection)     | `[1, 2, 3]`              |
# | tuple           | Tuple (immutable collection)  | `(1, 'apple', 3.14)`     |
# | set             | Set (unordered collection)    | `{1, 2, 3}`              |
# | dict            | Dictionary (key-value pairs)  | `{'name': 'John', 'age': 30}` |
# | NoneType        | None (represents absence)     | `None`                   |
# 
# # Python Reserved Words
# | Keyword     | Keyword                       | Keyword                     |
# |-----------------|-------------------------------|--------------------------|
# | if/else/elif/for/ while /return              | def        | pass/break /continue                 | is /as/not
# |    in     |import /from |  try/yield            |
# 

# %%
print('This is my first python code')

# %%
name= ' your name'
print(name)

# %%
# Variables and Data Types:
name = "John" # name is a variable of type string
age = 30 # age is a variable of type integer
height = 6.2 # height is a variable of type float
is_student = False # is_student is a variable of type boolean

print(name)
print(age)
print(height)
print(is_student)



# %%
print(type(name))

# %%
# show the type of each variable
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# %%
# print all variables in one line
print(name, age, height, is_student)
# or
print(name + " " + str(age) + " " + str(height) + " " + str(is_student))
# or f-string
print(f"{name} {age} {height} {is_student}")

# %%
print('your name','30')

# %% [markdown]
# # Operators

# %%
30*10

# %%
# Arithmetic Operators
x = 10
y = 5

addition_result = x + y
print("Addition:", addition_result)  # Output: 15

subtraction_result = x - y
print("Subtraction:", subtraction_result)  # Output: 5

multiplication_result = x * y
print("Multiplication:", multiplication_result)  # Output: 50

division_result = x / y
print("Division:", division_result)  # Output: 2.0

exponentiation_result = x ** y
print("Exponentiation:", exponentiation_result)  # Output: 100000

# %%
# Arithmetic Operators
x = 10
y = 5

addition_result = x + y
print("Addition:", addition_result)  # Output: 15

subtraction_result = x - y
print("Subtraction:", subtraction_result)  # Output: 5

multiplication_result = x * y
print("Multiplication:", multiplication_result)  # Output: 50

division_result = x / y
print("Division:", division_result)  # Output: 2.0

exponentiation_result = x ** y
print("Exponentiation:", exponentiation_result)  # Output: 100000

floor_division_result = x // y
print("Floor Division:", floor_division_result)  # Output: 2

# Bitwise Operators
a = 5  # Binary: 101
b = 3  # Binary: 011

bitwise_and_result = a & b
print("Bitwise AND:", bitwise_and_result)  # Output: 1 (Binary: 001)

bitwise_or_result = a | b
print("Bitwise OR:", bitwise_or_result)  # Output: 7 (Binary: 111)

bitwise_xor_result = a ^ b
print("Bitwise XOR:", bitwise_xor_result)  # Output: 6 (Binary: 110)

bitwise_left_shift_result = a << 1
print("Bitwise Left Shift:", bitwise_left_shift_result)  # Output: 10 (Binary: 1010)

bitwise_right_shift_result = a >> 1
print("Bitwise Right Shift:", bitwise_right_shift_result)  # Output: 2 (Binary: 10)

# Comparison Operators
x = 10
y = 5

less_than_or_equal = x <= y
print("Less than or equal to:", less_than_or_equal)  # Output: False

greater_than = x > y
print("Greater than:", greater_than)  # Output: True

greater_than_or_equal = x >= y
print("Greater than or equal to:", greater_than_or_equal)  # Output: True

not_equal = x != y
print("Not equal to:", not_equal)  # Output: True

equal_to = x == y
print("Equal to:", equal_to)  # Output: False

# Assignment Expression
if (n := len("hello")) > 4:
    print(f"The length of 'hello' is {n}.")  # Output: "The length of 'hello' is 5."

# Matrix Multiplication Operator
import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_product = matrix_a @ matrix_b
print("Matrix Product:")
print(matrix_product)


# %% [markdown]
# ## Most used python data structures are list and Dictionary
# ## 1.  List

# %%
# list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# %%
mix_list=['apple', 3, 'banana', 4, 'cherry', 5]
print(mix_list)

# %%
# check data type
print(type(fruits))

# %% [markdown]
# ## 2. Dictionaries:

# %%
#Dictionaries:
person = {"name": "Alice", "age": 25, "city": "New York"}
print(type(person))
print(person["name"])  # Accessing values
person["occupation"] = "Engineer"  # Adding key-value pairs


# %%
person.keys()  # Accessing keys

# %%
person.values()  # Accessing values

# %% [markdown]
# ## Add function from built-in library or third-party library

# %%
# Add function from built-in library or third-party library
from math import sqrt
print(sqrt(25))


# %%
# list of numbers
numbers = [1, 4, 9]
# square root of each number
roots = [sqrt(n) for n in numbers]
print(roots)

# %% [markdown]
# ## D

# %%
# Define your own function 
def my_square(n):
    return n ** 2
print(my_square(5))


# %%
# or
def greet(name):
    return "Hello, " + name + "!"

result = greet("Bob")
print(result)

# %% [markdown]
# ## Accessing items from list and Dictionary
# 
# ## Accessing, Indexing, Adding, and Deleting Items Cheatsheet
# 
# ## Lists
# 
# | Operation                         | Code Example                     | Description                                                      |
# |-----------------------------------|----------------------------------|------------------------------------------------------------------|
# | Accessing an element by index     | `my_list[index]`                 | Retrieves the element at the specified index in the list.       |
# | Slicing                           | `my_list[start:stop:step]`       | Extracts a portion of the list based on start, stop, and step.   |
# | Accessing the last element        | `my_list[-1]`                    | Accesses the last element of the list.                           |
# | Adding an item at the end         | `my_list.append(item)`           | Appends an item to the end of the list.                          |
# | Inserting an item at an index     | `my_list.insert(index, item)`    | Inserts an item at the specified index in the list.             |
# | Removing an item by value         | `my_list.remove(item)`           | Removes the first occurrence of the item with the given value.  |
# | Removing an item by index         | `del my_list[index]`             | Deletes the item at the specified index.                        |
# | Checking if an item exists        | `item in my_list`                | Checks if an item exists in the list.                            |
# | Finding the index of an item     | `my_list.index(item)`            | Returns the index of the first occurrence of the item.           |
# 
# ## Dictionaries
# 
# | Operation                         | Code Example                     | Description                                                      |
# |-----------------------------------|----------------------------------|------------------------------------------------------------------|
# | Accessing a value by key          | `my_dict[key]`                   | Retrieves the value associated with the specified key.           |
# | Adding a key-value pair           | `my_dict[key] = value`           | Inserts a new key-value pair into the dictionary.                |
# | Removing a key-value pair         | `del my_dict[key]`               | Deletes the key-value pair with the specified key.               |
# | Checking if a key exists          | `key in my_dict`                 | Checks if a key exists in the dictionary.                         |
# | Getting all keys                  | `my_dict.keys()`                 | Returns a list of all keys in the dictionary.                    |
# | Getting all values                | `my_dict.values()`               | Returns a list of all values in the dictionary.                  |
# | Getting key-value pairs           | `my_dict.items()`                | Returns a list of key-value pairs as tuples.                     |
# 
# 

# %%
# Creating a sample list
# here 1=0, 7=1,3=2
my_list = [1, 7, 3, 4, 5]
# Accessing an element by index
my_list[1]  

# %%
# Slicing
my_list[1:4]  

# %%
# Accessing the last element
my_list[-1]  

# %%
# Adding an item at the end
my_list.append(11)
my_list 

# %%
# Inserting an item at an index
my_list.insert(2,88)  # 2 is the index, 7 is the value
my_list

# %%
# Removing an item by value
my_list.remove(4)
my_list

# %%
# Creating a sample dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict # keys and values

# %%
# print all keys
my_dict.keys()

# %%
# print all values
my_dict.values()

# %%
# Accessing a value by key
my_dict['age']

# %%
# Adding a key-value pair
my_dict['job'] = 'Engineer' 

# %%
my_dict

# %%
# Removing a key-value pair
del my_dict['city']
my_dict

# %%
# merge two dictionaries
my_dict1 = {'name': 'John', 'age': 30}
my_dict2 = {'city': 'New York', 'job': 'Engineer'}
my_dict1.update(my_dict2)
my_dict1

# %%
# merge two lists
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list1.extend(my_list2)
my_list1

# %%
# add two lists with different length,differnt data type
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6, 7]
# string
my_list3 = ['a', 'b', 'c']

my_list1 + my_list2 # numbers
my_list1 + my_list3 # numbers and string

# %%
my_list1 + my_list2 # numbers

# %%
my_list1 + my_list3 

# %% [markdown]
# # Control: if / for /while 

# %%
#Conditional Statements (if-else):
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greater than 5")


# %%
# Example using a for loop
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

# %%
# alternative way in one line ; list comprehension : [expression for item in list]
[print(fruit) for fruit in fruits]

# %%
# Example using a for loop with range: range is a built-in function that returns a sequence of numbers
for i in range(1, 6):
    print(i)
# alternative way in one line
[i for i in range(1, 6)]

# %%
# Example using a while loop
count = 0 # initialize count to 0
while count < 6: # condition:  continue to run until condition is false
    print(count) # print count
    count += 1 # increment count by 1
    # this is equivalent to count = count + 1, it will keep adding 1 to count until count = 5


# %%
# Example using a while loop with break and continue
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue  # Skip iteration when num is 5 which means it will not print 5
    print(num)
    if num == 8:
        break  # Exit the loop when num is 8 which means it will not print 9 and 10

# %% [markdown]
# # Date time

# %%
import datetime
datetime.datetime.now()

# %%
# datetime 
date='2020-01-01'
date = datetime.datetime.strptime(date, '%Y-%m-%d')
print(date)
print(type(date))

# %%
# get month, day, year
print(date.month)
print(date.day)
print(date.year)

