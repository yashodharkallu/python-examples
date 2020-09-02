"""
# Generators are used to create iterators, but with a different approach
# Generators are simple functions which return an iterable set of items, one at a time, in a special way.
# Lazy iterator
# Similar to List comprehensions
# Memory footprint: Here it doesn't store all values in RAM. Constant size
"""

# List Comprehension
nums = [1,2,3]
squares=[num*num for num in nums]

print("List Comprehension way: ", squares)


# Generator Comprehension
nums = [1,2,3]
squares=(num*num for num in nums)
# Each time a __next__ is called

print("List Comprehension way: ", [*squares])

# A function with yield is a generator function
# lazy function
def gen_squares(nums):
    for num in nums:
        yield  num*num

print("Generator :",[*gen_squares([1,2,3])])