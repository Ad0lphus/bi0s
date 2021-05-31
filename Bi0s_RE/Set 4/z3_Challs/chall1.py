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