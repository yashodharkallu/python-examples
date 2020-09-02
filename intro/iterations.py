print("__________________________Iterating Through an Iterator next()__________________________________")
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
# next(my_iter)

print("__________________________Printing sum till 20 using while() loop_______________________________")
a = 10  # Initialization
while a <= 20:  # Condition  -- used for linkedList or DB queries.When you do not know when to exit
    print(a)
    a = a + 2   # Increment

print("__________________________Printing sum till 20 using while() with else loop____________________")
x = 1
while (x < 5):
   print('inside while loop value of x is ', x)
   x = x + 1
else:
   print('inside else value of x is ', x)

print("__________________________for loop_____________________________________________________________")
# for loop - when both initial and termination condition is known to us, e.g. iterating collectionz
for c in range(1, 10):
    print(c)

print("__________________________for loop using list________________________________________________")
lang = ("Python", "C", "C++", "Java")
for i in range(len(lang)):
   print(lang[i])

print("__________________________for loop using list________________________________________________")

a_list = ["a", "b", "c", "d"]

for iteration, item in enumerate(a_list):
    if iteration == 2:
        break
    else:
        print(iteration, item)

print("_________________________Building Custom Iterators____________________________________________")
# Building an iterator from scratch is easy in Python.
# We just have to implement the __iter__() and the __next__() methods


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))