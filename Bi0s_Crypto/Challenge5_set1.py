a=b"Burning 'em, if you ain't quick and nimble"
b=b"ICE"
c=b"I go crazy when I hear a cymbal"
def func(a,b):
    o=b''
    c=0
    for i in a:
        o+=bytes([i^ b[c]])
        if c+1==len(b):
            c=0
        else:
            c+=1
    return o
print(func(a,b).hex())
print(func(c,b).hex())

