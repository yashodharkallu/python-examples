from collections import Counter as counter

for _ in range(int(input())):
    n = int(input())
    boxes = list(map(int, input().split()))
    k = int(input())
    c = counter(boxes)
    ways = 0
    for i in range(1, k // 2 + 1):
        v1 = c.get(i)
        v2 = c.get(k - i)
        if v1 is not None and v2 is not None:
            if i != k - i:
                ways += (v1 * v2)
            else:
                ways += (v1 * (v1 - 1) // 2)
    print(ways)

