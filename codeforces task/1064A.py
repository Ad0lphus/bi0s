l= input().split(' ')
a = int(l[0])
b = int(l[1])
c = int(l[2])
m = max(a,b,c)
d = a+b+c-m
if d > m:
  print(0)
else:
  print(m-d+1)
