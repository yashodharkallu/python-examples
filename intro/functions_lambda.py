"""
# Anonymous Function: lambda f, t: f(*t)
# map,filter,reduce

# In this program we will learn what Python lambda is.
# The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without
# a name. These functions are throw-away functions, i.e. they are just needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). The lambda
# feature was added to Python due to the demand from Lisp programmers.

# The argument list consists of a comma separated list of arguments and the expression is an arithmetic
# expression using these arguments. You can assign the function to a variable to give it a name.
# The following example of a lambda function returns the sum of its two arguments:
"""

my_func = lambda x, y: x * y
# returns 6
print(my_func(2, 3))

# example to find squares of all numbers from a list
my_list = [i for i in range(10)]
# returns square of each number
my_func = lambda x: x * x

squares = list(map(my_func, my_list))
print(squares)              # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Function as a argument
def calculate(f, x, y):
    return f(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print("Add :", calculate(add, 10, 20))
print("Subtract : ", calculate(sub, 10, 20))

# Anonymous Function: lambda f, t: f(*t)
print("Add : ", calculate(lambda x, y: x + y, 10, 20))
print("Subtract : ", calculate(lambda x, y: x - y, 10, 20))


# Structural Programming
def increment(x):
    return x + 1


def increment_each(elements):
    result = []
    for element in elements:
        result.append(increment(element))
    return result


print("Incrementing a list in a procedural way ", increment_each([1, 9, 3]))

# Functional programming
# [*map(chr, [66, 53, 0, 94])]
# Thanks to Additional Unpacking Generalizations
print("Incrementing a list in functional way ", [*map(increment, [1, 9, 3])])

