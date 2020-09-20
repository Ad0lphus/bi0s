x=y=0
for i in range(5):
  r=input().split()
  for j in range(5): 
    if r[j]=='1':
      x,y=i,j
print(abs(x-2)+abs(y-2))
