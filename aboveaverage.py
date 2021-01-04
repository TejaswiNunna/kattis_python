t = int(input())
count = 0
tot_list = []
for i in range(1,t+1):
    x = [int(x) for x in input().split()]
    del x[0]
    average_mark = sum(x) / len(x)
    for j in x:
        if j > average_mark:
            count += 1
    tot_list.append(count/len(x)*100)
    count = 0
for p in tot_list:
    print("%.3f" %p,"%",sep='')