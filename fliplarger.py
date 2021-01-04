a,b = input().split()
b = b[::-1]
a = a[::-1]
if a > b:
    print(int(a))
else:
    print(int(b))