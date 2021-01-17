a = tuple("abcde")
a,b,c,d,e = a
b = c = '*'
a = (a,b,c,d,e)
print(a)
