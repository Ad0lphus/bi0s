BITS 32

extern printf
extern scanf

section .rodata
        in: db "%d",0
        p: db "yes, it is prime",10,0
        np: db "NO, its not prime",10,0

section .text
        global main
        
        main:
        push ebp
        mov ebp, esp
        
        lea eax,[ebp-0x4]
        push eax
        push in
        call scanf
        
        mov ebx,DWORD[ebp-0x4]
        mov ecx,2
        
        LOOP:
        mov edx,0
        mov eax,ebx
        div ecx
        cmp edx,0

        je no
        add ecx,1
        cmp ecx,ebx

        jl LOOP
        push p
        call printf
        jmp end
        
        no:
        push np
        call printf
        
        end:
        leave
        ret