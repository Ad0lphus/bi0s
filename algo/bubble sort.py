#bubble sort - sorting algoritham by swapping the adjacent elements if they are in wrong order.

def bubbleSort(l):
  n=len(l)
  for i in range (n):
    for j in range (0,n-i-1):
      if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
        
#l=eval(input("enter list/arr: "))
#bubbleSort(l)
#print(l)

        
