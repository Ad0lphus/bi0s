s=input()
l=sorted(map(int,input().split()))
s=c=0
while s<=sum(l):
    s+=l.pop()
    c+=1
print(c)
