#!/usr/bin/python
"""
MUTABLE
List is an ordered, heterogeneous, and mutable python container. It is created with ‘[]’.
"""

weekdays = ["Mon", "Tue", "Wed", "Thus", "Fri"]
weekends = ["Sat", "Sun"]
days = weekdays + weekends

print("days :", days)
print("days + weekends :", weekdays + weekends)
print("days + weekends :", weekdays.__add__(weekends))

day_indices = [1, 2, 3, 4, 5, 6, 7]
zipped = zip(days, day_indices)
print("zip days and day indices: ", list(zipped))

print("weekdays head = ", weekdays[0])
print("weekdays tail = ", weekdays[-1])
print("weekdays's 2nd index = ", weekdays[1])
print("weekdays contains 'Mon'? ", "Mon" in weekdays)
print("weekdays contains 'Mon'? ", weekdays.__contains__("Mon"))
print('weekdays from 1st Index to 3rd Index:', weekdays[1: 4])
print("weekdays size = ", weekdays.__sizeof__(), "bytes")
print("No of days = ", len(weekdays))
weekdays.reverse()
print("Reverse of weekdays = ", weekdays)
weekdays.reverse()
print('Index of element \'Wed\':', weekdays.index("Wed"))

print("~~~~~~~~~~~~~~~~~~~~~~~ Iterate  ~~~~~~~~~~~~~~~~~~~~~~~")
print(' ~ '.join(str(day) for day in days))  # comprehensions and generators over map()

print("~~~~~~~~~~~~~~~~~~~~~~~ List comprehension ~~~~~~~~~~~~~~~~~~~~~~~")
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension:
numbers = [i for i in range(10)]
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [i * i for i in range(10)]
print(squares)              # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("################################### num List ###############################################")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index   0  1  2  3  4  5  6  7  8
#        -9 -8 -7 -6 -5 -4 -3 -2 -1

# List Slicing
print('Original List:', my_list)
# Prints the 0th element of the list
print('First Element:', my_list[0])
# Prints the 2nd element of the list
print('Element at 2nd Index position:', my_list[2])
# Prints elements of the list from 0th index to 4th index. IT DOESN'T INCLUDE THE LAST INDEX
print('Elements from 0th Index to 4th Index:', my_list[0:5])
# Prints the -7th or 3rd element of the list
print('Element at -7th Index:', my_list[-7])

# To append an element to a list
my_list.append(10)
print('Append:', my_list)

# To find the index of a particular element
print('Index of element \'6\':', my_list.index(6))  # Returns index of element '6'

# To sort the list
new_list = [2, 3, 1, 8, 7]
new_list.sort()
print('Sorted list: ', new_list)

# To pop last element
print('Popped Element:', my_list.pop())

# To remove a particular element from the lsit BY NAME
my_list.remove(6)
print('After removing \'6\':', my_list)

# To insert an element at a specified Index
my_list.insert(5, 6)
print('Inserting \'6\' at 5th index:', my_list)

# To count number of occurences of a element in the list
print('No of Occurences of \'1\':', my_list.count(1))

# To extend a list that is insert multiple elements at once at the end of the list
my_list.extend([10, 11])
print('Extended list:', my_list)

# To reverse a list
my_list.reverse()
print('Reversed list:', my_list)
