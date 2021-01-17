def isPrime(number):
    counter = 0
    for n in range(1, (number + 1)):
        if number % n == 0:
            counter += 1
    return (counter == 2)

numbers = range(1, 10001)
primeNumCounter = 0
for number in numbers:
    if isPrime(number):
        primeNumCounter += 1

print("# of prime numbers: {}".format(primeNumCounter))
