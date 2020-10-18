"""
# Generators are used to create iterators, but with a different approach
# Generators are simple functions which return an iterable set of items, one at a time, in a special way.
# Lazy iterator
# Similar to List comprehensions
# Memory footprint: Here it doesn't store all values in RAM. Constant size
"""

nums = [1, 2, 3, 4, 5]

print('Calculate square without using - Generator:')
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers(nums)
print(my_nums)

print('\nCalculate square using - Generator:')
def square_numbers_generator(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers_generator(nums)
print(my_nums)
# print(next(my_nums))
for num in my_nums:
    print(num)

print('\nCalculate square using - List Comprehension:')
# I want 'n*n' for each 'n' in nums
my_nums = [n*n for n in nums]
print(my_nums)

print('\nCalculate square using - map + lambda,')
my_nums = map(lambda n: n*n, nums)
for num in my_nums:
    print(num)

print('\nGet list of even numbers using - filter + lambda,')
my_nums = filter(lambda n: n % 2 == 0, nums)
for num in my_nums:
    print(num)

print()
my_nums = [n for n in nums if n % 2 == 0]
for num in my_nums:
    print(num)


