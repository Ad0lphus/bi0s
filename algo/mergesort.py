def mergeSort(l):
  if len(l)>1:
    mid=len(l)//2
    lt=l[:mid]
    rt=l[mid:]
    mergeSort(lt)
    mergeSort(rt)
    i,j=0,0
    k=0
    while i<len(lt) and j<len(rt):
      if lt[i]<rt[j]:
        l[k]=lt[i]
        i+=1
      else:
        l[k]=rt[j]
        j+=1
      k+=1
    while i<len(lt):
      l[k] = lt[i]
      i +=1
      k +=1
    while j<len(rt):
      l[k]=rt[j]
      j+=1
      k+=1
  
l=eval(input("enter a list/arr: "))
mergeSort(l)
print(l)   
  
