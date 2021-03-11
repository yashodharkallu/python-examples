"""
This PEP proposes to add a pattern matching statement to Python, inspired by similar syntax found in Scala and many other languages.
https://www.python.org/dev/peps/pep-0622/

Under the proposal, this is how you could write classify:
def classify(entity):
  match entity:
    case Product(price=price):
      print("A Product that's {} INR cost ".format(age))
    case Customer(name=name):
      print("A Customer named {}".format(name))

In other words, pattern matching allows you to inspect a piece of data and simultaneously match its shape and bind the value of its fields to variables. In the above code, Cat(age=age) is a pattern that matches Cat values, and binds to the variable named age.
"""
import re


class Customer:
    def __init__(self, name):
        self.name = name


class Product:
    def __init__(self, price):
        self.price = price


def classify(entity):
    if isinstance(entity, Product):
        print("A Product that's {} INR cost ".format(entity.price))
    elif isinstance(entity, Customer):
        print("A Customer named {}".format(entity.name))


classify(Customer("Rohit"))
# prints: A Customer named Rohit

classify(Product(3000))
# prints: A Product that's 3000 INR cost

#######################################################################################################


print("\n################# re.match() ########################")
pattern = '^R\\w+\\W+\\w+n$'
test_string = 'Ravi Kiran'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

print("\n################# re.findall() ########################")
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

print("\n################# re.split() ########################")
result = re.split(pattern, string)
print(result)

print("\n################# re.sub() ########################")
# Program to remove all whitespaces

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)

print("\n################# re.search() ########################")
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")


print("\n################# re.search() match.group() ########################")
date_string = '2021-02-18'

# Three digit number followed by space followed by two digit number
date_pattern = '(\d{4})-(\d{2})-(\d{2})'

# match variable contains a Match object.
match = re.search(date_pattern, date_string)

if match:
  print('year: ', match.group(1))
  print('month: ', match.group(2))
  print('date: ', match.group(3))
else:
  print("pattern not found")