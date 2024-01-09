# # Day 2 Advanced Python concepts

# %% [markdown]
# 1. Function Definition:
# 
# ** def ** : Keyword used to define a function.
# function_name: Name of the function. Follows the same rules as variable names.
# (parameter1, parameter2, ...): Parameters that the function takes as input. These are optional.
# 
# 2. Docstring:
# 
# Triple-quoted string immediately below the function definition. Provides documentation for the function.
# Describes what the function does, explains the purpose of parameters, and specifies the return value.
# Not mandatory but considered good practice for code documentation.
# 
# 3. Parameters:
# 
# List of parameters inside the parentheses. Parameters are placeholders for values that the function expects to receive when called.
# Each parameter has a name and a type annotation (e.g., parameter1 (type)).
# Descriptions of each parameter explain what values they should represent.
# 
# 4. Function Body:
# 
# Contains the actual code that defines the functionality of the function.
# Can include statements, expressions, conditionals, loops, etc.
# This is where the main work of the function is done.
# 
# 5. Return Statement:
# 
# return: Keyword used to specify the result that the function should provide back to the caller.
# result_value: The value or object that the function returns.
# The return statement is optional. If omitted, the function returns None by default.

# %%
def add_numbers(x, y):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    - x (int or float): The first number.
    - y (int or float): The second number.
    
    Returns:
    - float: The sum of x and y.
    """
    result = x + y
    return result
# call function
add_numbers(5, 10)

# %%
import math
def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    """
    return math.factorial(n)
print(calculate_factorial(5))

# %%
def factorial(n):
    """
    Calculates the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Call the function
factorial_result = factorial(5)
print(f"The factorial is: {factorial_result}")


# %%
def add_numbers(a, b):
    """Adds two numbers."""
    return a + b

result = add_numbers(3, 5)
print(result) 

# %%
add = lambda x, y: x + y
result = add(3, 5)

print(result)

# %%
def calculator(operation):
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    else:
        return None

add_function = calculator("add")
result_add = add_function(3, 4)

subtract_function = calculator("subtract")
result_subtract = subtract_function(7, 2)

print(result_add)      # Output: 7
print(result_subtract) # Output: 5


# %%
def read_and_print_file(file_path):
    """
    Reads and prints lines from a text file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Test the function
read_and_print_file('example.txt')
# Assumes 'example.txt' contains some lines of text


# %%
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)

print(mean_value)

# %%
#mymodule.py:
def greet(name):
    """Prints a greeting."""
    print(f"Hello, {name}!")

def square(x):
    """Returns the square of a number."""
    return x ** 2
# import mymodule

# mymodule.greet("Alice")  # Output: Hello, Alice!
# result = mymodule.square(4)
# print(result)  # Output: 16

# %% [markdown]
# # Some special functions and built-in functions in Python, including map, zip, filter, and reduce
# 
#  They are built-in functions in Python that provide powerful tools for working with sequences and collections.
# 
# # Key Differences:
# 
# ## Output Type:
# 
# - `map()`, `filter()`: Return iterable data structures like lists.
# - `zip()`: Returns an iterable of tuples.
# - `reduce()`: Returns a single value.
# 
# ## Functionality:
# 
# - `map()`: Applies a function to each element independently.
# - `zip()`: Combines elements from multiple iterables.
# - `filter()`: Selectively includes elements based on a condition.
# - `reduce()`: Aggregates values using a binary function cumulatively.
# 
# ## Use Cases:
# 
# - Use `map()` when you want to transform each element in an iterable.
# - Use `zip()` when you want to combine elements from different iterables.
# - Use `filter()` when you want to selectively include elements based on a condit
# 

# %%
numbers = [1, 2, 3, 4, 5]
# use of map without lambda
def square(x):
    return x**2
squared = map(square, numbers) # map(function, iterable)
print(list(squared))

# %%
# Using map to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers) # map(function, iterable)
print(list(squared))

# %%
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

zipped_data = zip(names, scores) # zip(iterable1, iterable2)
zipped_list = list(zipped_data)
print(zipped_list)  #


# %%
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers) # filter(function, iterable)
even_list = list(even_numbers)
print(even_list)  

# %%
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers) # reduce(function, iterable)
print(product)  

# %% [markdown]
# | Regular Expression Pattern  | Description                                      |
# | --------------------------- | ------------------------------------------------ |
# | `.`                         | Matches any character except a newline          |
# | `^`                         | Matches the start of a string                    |
# | `$`                         | Matches the end of a string                      |
# | `*`                         | Matches 0 or more occurrences of the preceding character |
# | `+`                         | Matches 1 or more occurrences of the preceding character |
# | `?`                         | Matches 0 or 1 occurrence of the preceding character |
# | `\d`                        | Matches any digit (0-9)                         |
# | `\D`                        | Matches any non-digit character                  |
# | `\w`                        | Matches any word character (alphanumeric or underscore) |
# | `\W`                        | Matches any non-word character                  |
# | `\s`                        | Matches any whitespace character                |
# | `\S`                        | Matches any non-whitespace character            |
# | `[abc]`                     | Matches any character a, b, or c                |
# | `[^abc]`                    | Matches any character except a, b, or c         |
# | `[a-z]`                     | Matches any lowercase letter                     |
# | `[A-Z]`                     | Matches any uppercase letter                     |
# | `[0-9]`                     | Matches any digit (0-9)                         |
# | `(abc)`                     | Groups and captures the enclosed pattern       |
# | `|`                         | Acts as a logical OR for patterns               |
# | `\b`                        | Matches a word boundary                          |
# | `\B`                        | Matches a non-word boundary                      |
# 

# %%
# simple example of regular expression
import re
pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")

# %%
# example of regular expression
txt = "The rain in starkville is good"
x = re.split("\s", txt)
print(x)

# %%
import re
# Sample text containing phone numbers
text = "Please contact us at 123-456-7890 or 555-555-5555 for assistance."

# Define a regular expression pattern for matching phone numbers
pattern = r'\d{3}-\d{3}-\d{4}'

# Use the findall method to find all matches in the text
phone_numbers = re.findall(pattern, text)
print(phone_numbers)  

# %%


# Sample text containing email addresses
text = "Please contact support@example.com for assistance or john.doe@email.co for more information."

# Define a regular expression pattern for matching email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Use the findall method to find all matches in the text
email_addresses = re.findall(pattern, text)

# Print the extracted email addresses
for email in email_addresses:
    print(email)