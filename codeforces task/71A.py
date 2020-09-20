n=int(input())
l,l1=[],[]
for i in range(n):
  l.append(input())
for j in l:
  if len(j)<11:
    l1.append(j)
  else:
    s=''
    f,l=j[0],j[-1]
    le=len(j)-2
    s=s+f+str(le)+l
    l1.append(s)
for x in l1:
  print(x)
    
    

  
