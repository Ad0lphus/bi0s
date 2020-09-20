s=input()
size=len(s)
s=s+''
c=0
f=0

for i in range(0,size-1):
  if s[i]=='0':
    if s[i+1]=='0':
      c=c+1
    elif s[i+1]=='1':
      c=0
    if c>=6:
      print("YES",end='')
      f=1
      break
  elif s[i]=='1':
    if s[i+1]=='1':
      c=c+1
    elif s[i+1]=='0':
      c=0
    if c>=6:
      print("YES",end='')
      f=1
      break
if f==0:
  print("NO")
    
