import re

a = input()
out = re.findall('[A-Z]',a)
print(''.join(out))