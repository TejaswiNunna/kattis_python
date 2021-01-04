n = int(input())
qaly = 0
for i in range(1,n+1):
    var1, var2 = [float(x) for x in input().split()]
    tot = var1 * var2
    qaly += tot
    i += 1

print(qaly)