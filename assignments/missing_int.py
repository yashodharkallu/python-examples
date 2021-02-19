# Python3 program to find missing k numbers in an array.

# Prints first k natural numbers in arr[0..n-1]
def printKMissing(arr, n, k):
    list(set(arr)).sort()
    print(arr)

    # Find first positive number
    i = 0
    while (i < n) and (arr[i] <= 0):
        i = i + 1

    # Now find missing numbers between array elements
    count = 0
    curr = 1
    res = []
    while (count < k) and (i < n):
        if arr[i] != curr:
            res.append(curr)
            count = count + 1
        else:
            i = i + 1
        curr = curr + 1

    # Find missing numbers after maximum.
    while count < k:
        print(">> ", curr)
        res.append(curr)
        curr = curr + 1
        count = count + 1
    return res

# Driver code
arr = [2, 5, 6, 3, 5]
n = len(arr)
k = 5
print(printKMissing(arr, n, k))