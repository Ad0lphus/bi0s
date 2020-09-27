s1=input().lower()
s2=input().lower()
l=[]
l.append(s1)
l.append(s2)
l1=sorted(l)
if l[0]==l[1]:
  print(0)
elif l[0]==l1[0] and l[1]==l1[1]:
  print(-1)
elif l[0]==l1[1] and l[1]==l1[0]:
  print(1)
