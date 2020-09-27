n=int(input())
s=input()
s1=''
i,j=0,0
while i<n:
  s1+=s[i]
  j+=1
  i+=j
print(s1)
