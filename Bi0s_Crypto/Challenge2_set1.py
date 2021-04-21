def xor(bytes1,bytes2):
    a=b''
    s=zip(bytes1,bytes2)
    print()
    for b,c in s:
        a+=bytes([b^c])
    return a
print(xor(bytes.fromhex('1c0111001f010100061a024b53535009181c'),bytes.fromhex('686974207468652062756c6c277320657965')))
