data = "label"
flag = ''
for i in data:
    flag += chr(ord(i) ^ 13)
print('crypto{{{}}}'.format(flag))
