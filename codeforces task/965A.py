import math

s=input()
s=s.split(' ')
l=[]
for i in s:
  l.append(int(i))
k,n,s,p=l[0],l[1],l[2],l[3]

x=math.ceil(math.ceil(n/s)*k/p)
print(x)
