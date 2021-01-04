import sys

msg = sys.stdin.readlines()
input_list = [x[:-1] for x in msg]
for i, s in enumerate(input_list):
    a,b = [int(x) for x in input_list[i].split()]
    print(abs(a - b))