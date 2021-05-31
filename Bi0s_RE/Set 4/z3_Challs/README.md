# chall 1

```python=
from z3 import *
s=Solver()

def func1(x, y):
	s.add(x*2*(y^x)-y==int('0x2a6a',16))
	s.add(x>ord('U'))
	s.add(x<ord('`'))
	s.add(y>ord('`'))
	s.add(y<ord('p'))

def func2(x,y):
	s.add(x%y==7)
	s.add(y>ord('Z'))

def func3(x,y):
	s.add((y^x)+x/y==int("0x15",16))
	s.add(x<ord('d'))
	s.add(y<ord('x'))

def func4(x,y):
	v2=x<<32|x
	s.add((v2%y)+x==int('0x89',16))
	s.add(x>ord('s'))
	s.add(y<ord('d'))
	s.add(y==ord('_'))

def func5(x,y):
	s.add((x+y)^y==int('0xe1',16))
	s.add(x>ord('Z'))
	s.add(y<ord('Z'))

def func6(x,y,z):
	s.add(x<=y)
	s.add(y<=z)
	s.add(x>ord('U'))
	s.add(y>ord('n'))
	s.add(z>ord('s'))
	s.add(((y+z)^(x+y))==int('0x2c',16))
	s.add(((y+z)%x)+y==int('0xa1',16))
  
def func7(x, y, z):
	s.add(x>=y)
	s.add(y>=z)
	s.add(x<ord('x'))
	s.add(y>ord('Z'))
	s.add(z<ord('Z'))
	s.add(((x+z)^(y+z))==int('0x7a',16))
	s.add(((x+z)%y)+z==int('0x65',16))

def func8(x,y,z):
	s.add(x<=y)
	s.add(y<=z)
	s.add(z<ord('s'))
	s.add(((x+y)/z)*y==int('0x61',16))
	s.add((x-y)^z==-8*13)

def func9(x,y,z):
	s.add(x==y)
	s.add(y>=z)
	s.add(z<=99)
	s.add(z+x*(z-y)-x==int('-0x5a3',16))

def func10(x,y,z):
	s.add(x>=y)
	s.add(y>=z)
	s.add(y*(x+z+1)-z==int('0x3c9a',16))
	s.add(y>ord('Z'))
	s.add(y<ord('d'))

def func11(x,y,z):
	s.add(y>=x)
	s.add(x>=z)
	s.add(y>ord('d'))
	s.add(y<ord('i'))
	s.add(x+(y^(y-z))-z==int('0x46',16))
	s.add(((y+z)/x)+x==int('0x44',16))

def func12(x,y,z):
	s.add(x>=y)
	s.add(y>=z)
	s.add(y<ord('<'))
	s.add(z<=ord(','))
	s.add(x+(y^(z+y))-z==int('0x6f',16))
	s.add((y^(y-z))+y==int('0x65',16))

def func13(x,y,z):
	s.add(x<=y)
	s.add(y<=z)
	s.add(x>ord('('))
	s.add(y>ord('Z'))
	s.add(z<ord('n'))
	s.add(z+(y^(z+x))-x==int('0x10d',16))
	s.add((z^(y-x))+y==int('0xb9',16))

def func14(x,y,z):
	s.add(x>=z)
	s.add(y>=z)
	s.add(y<ord('d'))
	s.add(z>ord('Z'))
	s.add(x+(y^(y+x))-z==int('0xb9',16))

def func15(x,y,z):
    s.add(y>=z)
    s.add(y>=x)
    s.add(z>ord('_'))
    s.add( y<ord('n'))
    s.add(((y-x)*y^z)-x==int('0x4be',16))
    s.add(((z-y)*z^x)+y==-int('0x40a',16))
def is_valid(x):
    return Or(And(x>=ord('A'),x<=ord('Z')),And(x>=ord('a'),x<=ord('z')),And(x>=ord('0'),x<=ord('9')),And(x==ord('_')),And(x==ord('!')),And(x==ord('@')),And(x==ord('#')),And(x==ord('$')),And(x==ord('%')),And(x==ord('^')),And(x==ord('&')),And(x==ord('*')),And(x==ord('?')),And(x==ord(':')),And(x==ord('(')),And(x==ord(')')))

x=[]
for i in range(26):
	x+=[BitVec('a'+str(i),32)]
for i in range(26):
    s.add(is_valid(x[i]))
func1(x[0],x[1])
func2(x[1],x[2])
func3(x[2],x[3])
func4(x[3],x[4])
func5(x[4],x[5])
func6(x[5],x[6],x[7])
func7(x[7],x[8],x[9])
func8(x[9],x[10],x[11])
func9(x[11],x[12],x[13])
func10(x[13],x[14],x[15])
func11(x[15],x[16],x[17])
func12(x[17],x[18],x[19])
func13(x[19],x[20],x[21])
func14(x[21],x[22],x[23])
func15(x[23],x[24],x[25])
print("conditions ",s.check(),'isfied :)',sep='')
a=s.model()

d=dict()
for i in (str(a)[1:-1].split('\n')):
	s=(i.split(',')[0].split(' ='))
	d[int(s[0].split('a')[-1])]=int(s[1])
for j in sorted(d):
	print(chr(d[j]),end='')
```
## Output:
I was not able to run in my current OS<br>

![](https://i.imgur.com/kAT4ZtE.png)<br>

So, I tried with an older version of ubuntu to fix that error [ ubuntu 14.04 LTS ]<br>

![](https://i.imgur.com/zatEwns.png)

***Flag: What_You_Wanna_Be?:)_lc_la***
<hr>

# chall 2
```python=
from z3 import *
import gdb
l=[]
for i in range(int('0x19',16)):
	l+=[BitVec('a'+str(i),16)]

s=Solver()

s.add((l[int("0x14",16)]^0x2B)==l[7])
s.add(l[int("0x15",16)]-l[3]==-20)
s.add((l[2]>>6)==0)
s.add(l[int("0xd",16)]==int("0x74",16))
s.add(4* l[int("0xb",16)]==int("0x17c",16))
s.add(l[7]>>(l[int("0x11",16)]%8)==5)
s.add((l[6]^0x53)==l[int('0xe',16)])
s.add(l[8]==int("0x7a",16))
s.add(l[5]<<(l[9]%8)==int("0x188",16))
s.add(l[int("0x10",16)]-l[7]==int("0x14",16))
s.add(l[7]<<(l[int("0x17",16)]%8)==int("0xbe",16))
s.add(l[2]-l[7]==int("-0x2b",16))
s.add(l[int("0x15",16)]==int("0x5f",16))
s.add((l[2]^0x47)==l[3])
s.add(l[0]==int("0x63",16))
s.add(l[int("0xd",16)]==int("0x74",16))
s.add((l[int("0x14",16)]&0x45)==int("0x44",16))
s.add((l[8]&0x15)==int("0x10",16))
s.add(l[int("0xc",16)]==int("0x5f",16))
s.add(l[4]>>4==7)
s.add(l[int("0xd",16)]==int("0x74",16))
s.add(l[0]>>(l[0]%8)==int("0xc",16))
s.add(l[10]==int("0x5f",16))
s.add((l[8]&0xAC)==int("0x28",16))
s.add(l[int("0x10",16)]==int("0x73",16))
s.add((l[int("0x16",16)]&0x1D)==int("0x18",16))
s.add(l[9]==int("0x33",16))
s.add(l[5]==int("0x31",16))
s.add(4*l[int("0x13",16)]==int("0x1c8",16))
s.add(l[int("0x14",16)]>>6==1)
s.add(l[7]>>1==int("0x2f",16))
s.add(l[1]==int("0x6c",16))
s.add(l[3]>>4==7)
s.add((l[int("0x13",16)]&0x49)==int("0x40",16))
s.add(l[4]==int("0x73",16))
s.add(l[2]&l[int("0xb",16)]==int("0x14",16))
s.add(l[0]==int("0x63",16))
s.add(l[4]+l[5]==int("0xa4",16))
s.add(l[int("0xf",16)]<<6==int("0x17c0",16))
s.add(l[int("0xa",16)]^0x2B==l[int("0x11",16)])
s.add(l[int("0xc",16)]^0x2C==l[4])
s.add(l[int("0x13",16)]-l[int("0x15",16)]==int("0x13",16))
s.add(l[int("0xc",16)]==int("0x5f",16))
s.add(l[int("0xf",16)]>>1==int("0x2f",16))
s.add(l[int("0x13",16)]==int("0x72",16))
s.add(l[int("0x11",16)]+l[int("0x12",16)]==int("0xa8",16))
s.add(l[int("0x16",16)]==int("0x3a",16))
s.add(l[int("0x17",16)]&l[int("0x15",16)]==9)
s.add(l[6]<<(l[int("0x13",16)]%8)==int("0x18c",16))
s.add(l[3]+l[7]==int("0xd2",16))
s.add((l[int("0x16",16)]&0xED)==int("0x28",16))
s.add((l[int("0xc",16)] & 0xAC)==int("0xc",16))
s.add((l[int("0x12",16)]^0x6B)==l[int("0xf",16)])
s.add((l[int("0x10",16)]&0x7A)==int("0x72",16))
s.add((l[0]&0x39)==int("0x21",16))
s.add((l[6]^0x3C)==l[int("0x15",16)])
s.add(l[int("0x14",16)]==int("0x74",16))
s.add(l[int("0x13",16)]==int("0x72",16))
s.add(l[int("0xc",16)]==int("0x5f",16))
s.add(l[2]==int("0x34",16))
s.add(l[int("0x17",16)]==int("0x29",16))
s.add(l[int("0xa",16)]==int("0x5f",16))
s.add((l[int("0x16",16)]&l[9])==int('0x32',16))
s.add(l[3]+l[2]==int('0xa7',16))
s.add(l[int('0x11',16)]-l[int('0xe',16)]==int('0x44',16))
s.add(l[int('0x15',16)]==int('0x5f',16))
s.add((l[int('0x13',16)]^0x2D)==l[int('0xa',16)])
s.add(4*l[int('0xc',16)]==int('0x17c',16))
s.add(l[6]&0x40>=1)
s.add((l[int('0xc',16)]&l[int('0x16',16)])==int('0x1a',16))
s.add(l[7]<<(l[int('0x13',16)]%8)==int('0x17c',16))
s.add((l[int('0x14',16)]^0x4E)==l[int('0x16',16)])
s.add(l[6]==int('0x63',16))
s.add(l[int('0xc',16)]==l[7])
s.add(l[int('0x13',16)]-l[int('0xd',16)]==-2)
s.add(l[int('0xe',16)]>>4==3)
s.add((l[int('0xc',16)]&0x38)==int('0x18',16))
s.add(l[8]<<(l[int('0xa',16)]%8)==int('0x3d00',16))
s.add(l[int('0x14',16)]==int('0x74',16))
s.add(l[6]>>(l[int('0x16',16)]%8)==int('0x18',16))
s.add(l[int('0x16',16)]-l[5]==9)
s.add(l[7]<<(l[int('0x16',16)]%8)==int('0x17c',16))
s.add(l[int('0x16',16)]==int('0x3a',16))
s.add(l[int('0x10',16)]==int('0x73',16))
s.add((l[int('0x17',16)]^0x1D)==l[int('0x12',16)])
s.add(l[int('0x17',16)]+l[int('0xe',16)]==int('0x59',16))
s.add((l[5]&l[2])==int('0x30',16))
s.add((l[int('0xf',16)]&0x9F)==int('0x1f',16))
s.add(l[4]==int('0x73',16))
s.add((l[int('0x17',16)]^0x4A)==l[0])
s.add((l[6]^0x3C)==l[int('0xb',16)])

print("conditions ",s.check(),'isfied :)',sep='')
a=s.model()
print("input: ",end="")
#print(a)

d,s1=dict(),''
for i in (str(a)[1:-1].split('\n')):
	s=(i.split(',')[0].split(' ='))
	d[int(s[0].split('a')[-1])]=int(s[1])
for j in sorted(d):
	s1+=chr(d[j])
	print(chr(d[j]),end='')
print()
f=open('chall2.txt','w+')
f.write(s1)
print(f.read())
gdb.execute('file chall2')
gdb.execute('r < chall2.txt')
gdb.execute('q')
```

## Output:

![](https://i.imgur.com/CdXKzHz.png)


***Flag: shkCTF{cl4ss1c_z3___t0_st4rt_:)}***
<hr>

# rop-obf

```python=
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
```

## Output:

![](https://i.imgur.com/i3ZyY7O.png)<br>

***Input :***
4
8
15
16
23
42
