def test(l, retry=[]):
    print(l, retry)
    if (len(l) == 0) and (sum(retry) < 3):
        print('retry')
        retry.append(True)
        test([], retry)
    if (len(l) == 0) and (sum(retry) == 3):
        raise
    return 10
print(test([]))
#print(sum([]))