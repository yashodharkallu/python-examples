# pip3 install memory_profiler
import memory_profiler as mem_profile
import time


t1 = time.process_time()
m1 = mem_profile.memory_usage()[0]


def get_prime_num(N):
    result = []
    for num in range(N + 1):
        counter = 0
        for n in range(2, num):
            if num % n == 0:
                counter += 1
        if counter == 0:
            result.append(num)
    return result


def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        counter = 0
        for i in range(2, n):
            if n % i == 0:
                counter += 1
        if counter == 0:
            yield n



print(*gen_primes(100000))
# print(*get_prime_num(100000))
t2 = time.process_time()
m2 = mem_profile.memory_usage()[0]

print('Memory used: {} MB'.format(m2 - m1))
print('Took {} seconds'.format(t2 - t1))

# 9592
# Memory used: 0.01171875 MB
# Took 395.35502 seconds