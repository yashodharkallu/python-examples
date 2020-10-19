import sys
import itertools

n = int(sys.stdin.readline())

games = {}
for i in range(n):
    s = sys.stdin.readline().rstrip().split(',')
    games[s[0]] =  (int(s[1]), int(s[2]))

res = ()
maxpay = 0

for k in range(1, n):
    for z in itertools.combinations(games, k):
        time = 0
        pay = 0
        for x in z:
            time += games[x][0]
            if time > 120:
                break
            pay +=  games[x][1]
        if time <= 120 and pay > maxpay:
            res = z
            maxpay = pay

print('\n'.join(sorted(list(res))))