def solution(N):
    num = str(abs(N))
    small = False
    index = 0
    if N < 0:
        for i in num:
            index = index + 1
            if i >= '5':
                small = False
                break
        if small:
            return int(num[:index] + '5' + num[index:]) * -1
        else:
            return int(num[:index-1] + '5' + num[index-1:]) * -1
    else:
        for i in num:
            index = index + 1
            if i <= '5':
                small = True
                break
        if small:
            return int(num[:index-1] + '5' + num[index-1:])
        else:
            return int(num[:index] + '5' + num[index:])


print(solution(-777))
print(solution(-268))
print(solution(0))
print(solution(-676))
print(solution(777))
print(solution(268))
print(solution(0))
print(solution(676))
print(solution(8))