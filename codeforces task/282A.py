n=int(input())
c=0
for i in range(0,n):
  s=input()
  l=s.split('x')
  for j in l:
    if j=='++':
      c+=1
    elif j=="--":
      c-=1
print(c)
