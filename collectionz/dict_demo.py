#!/usr/bin/python
"""
MUTABLE
key-value pairs
Dictionary is an unordered, heterogeneous, and mutable python container. It is associated with a key-pair value. It can be indexed only by its keys.
"""

my_dict = {}
print("An Empty Dictionary: ", my_dict)
my_dict[0] = 'Apples'
my_dict[2] = 'Mangoes'
my_dict[3] = 20
print("\n3 elements have been added: ")
print(my_dict)

# Creating an empty dictionary:
dict_sample = {}

# Creating a dictionary with mixed keys:
dict_sample = {'fruit': 'mango', 1: [4, 6, 8]}

# Create a dictionary by explicitly calling the Python's dict() method:
dict_sample = dict({1: 'mango', 2: 'pawpaw'})

# created from a sequence as shown below:
dict_sample = dict([(1, 'mango'), (2, 'pawpaw')])

# Dictionaries can also be nested, which means that we can create a dictionary inside another dictionary.
# For example:
dict_sample = {1: {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'},
               2: {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}}

print("\n<<<<<Accessing Elements>>>>>")
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
print(dict_sample)

print(dict_sample["model"])

print("\n<<<<<Adding Elements>>>>>")
dict_sample["Capacity"] = "1800CC"
print(dict_sample)

print("\n<<<<<Updating Elements>>>>>")
dict_sample["year"] = 2014
print(dict_sample)

print("\n<<<<<Removing Elements>>>>>")
del dict_sample["year"]
print(dict_sample)
# Another way to delete a key-value pair is to use the pop() function
# and pass the key of the entry to be deleted as the argument to the function
dict_sample.pop("Capacity")
print(dict_sample)

print("\nNumber of elements in a dictionary:", len(dict_sample))

print("\n<<<<< items() Method iterate>>>>>")
for k, v in dict_sample.items():
  print(k, v)

print("\n<<<<< items() Method with update>>>>>")
# The object returned by items() can also be used to show the changes that have been implemented on the dictionary.
x = dict_sample.items()
print(x)
dict_sample["model"] = "Mark X"
print(x)

print("\n<<<<< keys() Method>>>>>")
# This method also returns an iterable object. The object returned is a list of all keys in the dictionary
x = dict_sample.keys()
print(x)
for k in dict_sample.keys():
  print(k)
