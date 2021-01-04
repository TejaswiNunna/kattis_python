import sys

msg = sys.stdin.readlines()
k = []
v = []
input_list = [x[:-1] for x in msg]
for i, s in enumerate(input_list):
    if input_list[i].startswith('def'):
        if input_list[i].split(' ')[1] in k:
            v[k.index(input_list[i].split(' ')[1])] = input_list[i].split(' ')[-1]
        else:
            k.append(input_list[i].split(' ')[1])
            v.append(input_list[i].split(' ')[-1])
    elif input_list[i].startswith('calc'):
        exp_main = ''
        exp = input_list[i][5:]
        for word in exp.split(' '):
            if word in k:
                exp_main += v[k.index(word)]
            else:
                exp_main += word
        try:
            tot = eval(exp_main[:-1])
            if str(tot) in v:
                print(exp,k[v.index(str(tot))])
            else: print(exp,"unknown")
        except:
            print(exp,"unknown")                
    else:
        k.clear()
        v.clear()