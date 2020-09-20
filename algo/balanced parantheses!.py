openpar=['(','[','{']
closepar=[')',']','}']
def checkpar(string):
  stack=[]
  for i in string:
    if i in openpar:
      stack.append(i)
    elif i in closepar:
      p=closepar.index(i)
      if (len(stack)>0 and openpar[p]==stack[-1]):
        stack.pop()
      else:
        return 'un balanced'
  if len(stack)==0:
    return 'balanced'
  else:
    return 'un balanced'
#({[]})
#string=input('enter a string: ')
#print(checkpar(string))
    
