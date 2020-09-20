def binary(l,a,b,x): 
  if b>=a:
    mid = (a+b)//2
    if l[mid]==x:
      return mid
    elif l[mid]>x: 
      return binary(l,a,mid-1,x) 
    else: 
      return binary(l,mid+1,b,x) 
  else:
    return -1
  

l=eval(input("enter a list:"))
x=eval(input("enter number:"))
n=binary(l,0,len(l)-1,x) 
if n !=-1: 
  print("Element found! pos: ",n+1) 
else:
  
  print("Element is not found") 
