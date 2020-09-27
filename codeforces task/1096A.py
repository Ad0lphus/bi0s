n=int(input())
print()
l=[]
for i in range(n):
  s=input()
  s=s.split()
  l.append(s[0])
for i in l:
  print(int(i),int(i)*2)
