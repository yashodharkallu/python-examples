#!/usr/bin/python
"""
MUTABLE
Set is also similar to a list, except it is unordered. It can store heterogeneous data and it is mutable. We create a set by enclosing our data with curly brackets ‘{}’.
Every set element is unique (no duplicates) and must be immutable (cannot be changed).
set cannot have mutable elements like lists, sets or dictionaries as its elements.

Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
While tuples are immutable lists, frozensets are immutable sets.
"""

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set cannot have duplicates
my_set = set("hello world")
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# convert list to set and vice versa
my_set = set([1, 2, 3, 2])
my_list = list({1, 1, 2, 3, 3})
print(my_set)
print(my_list)

# set cannot have mutable items
# here [3, 4] is a mutable list
# my_set = {1, 2, [3, 4]}

# Distinguish set and dictionary while creating empty set
# initialize a with {} and check data type
a = {}
print(type(a))

# initialize a with set() and check data type
a = set()
print(type(a))

print("\n<<<<<<<<<<< Modifying a set >>>>>>>>>")
# initialize my_set
my_set = {1, 3}
print(my_set)

# TypeError: 'set' object does not support indexing
# my_set[0]

# add an element
my_set.add(2)
print(my_set)

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)

# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)

print("\n<<<<<<<<<<< Removing elements from a set >>>>>>>>>")
# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)

# remove an element
my_set.remove(6)
print(my_set)

# discard an element not present in my_set
my_set.discard(2)
print(my_set)

# remove an element not present in my_set, you will get an error, KeyError
# my_set.remove(2)

print("\n<<<<<<<<<<< Set Union >>>>>>>>>>>>>")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator or or union() function
print(A | B)
print(A.union(B))

print("\n<<<<<<<<<<< Set Intersection >>>>>>>>>>>>>")
# use & operator or intersection() function
print(A & B)
print(A.intersection(B))

print("\n<<<<<<<<<<<  Set Difference >>>>>>>>>>>>>")
# use - operator or difference() function
print(A - B)
print(A.difference(B))

print("\n<<<<<<<<<<<  Set Symmetric Difference >>>>>>>>>>>>>")
# use ^ operator or symmetric_difference() function
print(A ^ B)
print(A.symmetric_difference(B))

print("\n<<<<<<<<<<<  Iterating Through a Set >>>>>>>>>>>>>")
for letter in set("apple"):
    print(letter)

