# pip3 install memory_profiler
import memory_profiler as mem_profile
import time

def isPrime(number):
    counter = 0
    for n in range(1, (number + 1)):
        if number % n == 0:
            counter += 1
    return (counter == 2)

numbers = range(1, 10001)
primeNumCounter = sum(1 for n in numbers if isPrime(n))

print("# of prime numbers: {}".format(primeNumCounter))
