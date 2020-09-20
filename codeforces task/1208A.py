n=int(input())
for i in range(n):
  s=input().split(" ")
  a,b,c=int(s[0]),int(s[1]),int(s[2])
  print([a,b,a^b][c%3])
