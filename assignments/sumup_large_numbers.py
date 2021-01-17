# Python3 program to find sum of two large numbers.

def findSum(num1, num2):
    if (len(num1) > len(num2)):
        t = num1
        num1 = num2
        num2 = t

    # Take an empty list for storing result
    result = []

    # Calculate length of both string
    n1 = len(num1)
    n2 = len(num2)

    # Reverse both of strings
    num1.reverse()
    num2.reverse()

    carry = 0
    for i in range(n1):
        # sum of current digits and carry
        sum = (num1[i] + (num2[i] + carry))
        result.append(sum)

        # Calculate carry for next step
        carry = int(sum / 10)

    # Add remaining digits of larger number
    for i in range(n1, n2):
        sum = (num2[i] + carry)
        result.append(sum % 10)
        carry = int(sum / 10)

    # Add remaining carry
    if carry:
        result.append(carry)

    # reverse resultant string
    result.reverse()
    return result

# Driver code
num1 = [1, 2]
num2 = [1, 9, 8, 1, 1, 1]
print(findSum(num1, num2))
