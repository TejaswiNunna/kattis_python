n = int(input())
tot = 0
for i in range(1,n+1):
    var =input()
    pow, num = var[-1], var[:-1]
    power = int(num) ** int(pow)
    tot += power
    i += 1

print(tot)