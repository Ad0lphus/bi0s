import gdb,os
def bit32():
    print("                                                         \n\nELF 32-bit LSB \n\n")

    global i
    for i in range(1,3001):
        try:
            gdb.execute('file '+str(i)+'.bin')
            xy=gdb.execute('info file',to_string=True)
            if "elf32" in xy:
                print("======================================================",i,"===============================================================================")
                print("file : ",i,".bin")
                print("Arch :  ELF 32-bit LSB")
                x=gdb.execute('disas 0x00000510,0x00000834',to_string=True).split('\n')[117].split(',')[-1]
                y=gdb.execute('disas 0x00000510,0x00000834',to_string=True).split('\n')[118].split(',')[-1]
                gdb.execute('file '+str(i)+'.bin')
                gdb.execute('r < temperoryStorage')
                xyz=gdb.execute('x/4bx 0x56557008',to_string=True).split(':')[1].replace('\t','').replace('\n','').replace(' ','').replace('0x','\\x')
                
            
        except:
            print("brrrrrrrrrrrrrrrrrrrr")

        chars,num=chr(int(y,16)),int(x,16)
        final=chars*num
        print("final:",final,"XYZ:",xyz)
        os.system('python -c print"\''+final+'\'+\''+xyz+'\'" > Pass')
        os.system('./'+str(i)+'.bin < Pass')



bit32()

gdb.execute("quit")