from z3 import *
import gdb

s=Solver()
l=[]
for i in range(6):
	l+=[BitVec(chr(i+97),64)]
s.add(l[0]^0x83==0x87)
s.add(l[1]^0x36==0x3e)
s.add(l[2]^0x9d==0x92)
s.add(l[3]^0xcd==0xdd)
s.add(l[4]^0xec==0xfb)
s.add(l[5]^0xf6==0xdc)
print("conditions ",s.check(),'isfied :)',sep='')
a=s.model()
l1,d,s1=(str(a)[1:-1].split(', ')),dict(),''
for i in l1:
	b=i.split('= ')
	d[b[0]]=int(b[1])
for j in sorted(d):
	s1+=str(d[j])+'\n'
	print(d[j])

f=open('rop.txt','w+')
f.write(s1)
print(f.read())
gdb.execute('file rop-obf')
gdb.execute('r < rop.txt')
gdb.execute('q')