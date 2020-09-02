print('Calculate square - without using Generator:')
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)


print('\nCalculate square - using Generator:')
def square_numbers_generator(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers_generator([1, 2, 3, 4, 5])
print(my_nums)
# print(next(my_nums))
for num in my_nums:
    print(num)


print('\nCalculate square - using List Comprehension:')
my_nums = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums)
for num in my_nums:
    print(num)

# Not of good performance, as all the elements to be loaded to the memory in 1 short
# print(list(my_nums))
