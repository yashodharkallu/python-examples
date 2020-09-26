"""
# Variable names are case-sensitive
"""
print("__________________________Assign Value______________________________________________________")
x = 1                       # x is an integer
print(type(x))
x = 'hello'                 # now x is a string
print(type(x))
x = [1, 2, 3]               # now x is a list
print(type(x))
x = {1: 'one', 2: 'two'}    # now x is a dict
print(type(x))
x = True
# False The false value of the bool type
# True The true value of the bool type
print(type(x))
x = None
# None The sole value of the type NoneType
print(type(x))

print("__________________________Assign Value to Multiple Variables_________________________________")
x, y, z = "Orange", 10.5, True
print(x)
print(y)
print(z)

print("__________________________Literals___________________________________________________________")
# Numeric Literals
a = 0b1010  # Binary Literals
b = 100     # Decimal Literal
c = 0o310   # Octal Literal
d = 0x12c   # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

print(a, b, c, d)
print(float_1, float_2)

# String literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string 
with more than 
one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Boolean literals
x = (1 == True)
y = (0 == False)
a = True + 4
b = False + 10

print("x:", x)
print("y:", y)
print("a:", a)
print("b:", b)

print("__________________________Constants__________________________________________________________")
import intro.constant as constant

print(constant.PI)
print(constant.GRAVITY)

print("__________________________How bool() works?__________________________________________________")
test = []
print(test, 'is', bool(test))

test = [0]
print(test, 'is', bool(test))

test = 0.0
print(test, 'is', bool(test))

test = None
print(test, 'is', bool(test))

test = True
print(test, 'is', bool(test))

test = 'Easy string'
print(test, 'is', bool(test))


a += 2          # a = a + 2
a -= 2          # a = a - 2
a *= 2          # a = a * 2
a /= 2          # a = a / 2

print("__________________________LEGB Rule: Local, Enclosing, Global, Built-in_______________________")
# This programs shows the rules for variable scope

x = 'Global x'


def test():
    # global x
    y = 'Local y'
    x = 'Local x'
    print(x + ', ' + y)  # prints 'Local x' and 'Local y'


if __name__ == '__main__':
    test()
    print(x)  # prints 'Global x'

