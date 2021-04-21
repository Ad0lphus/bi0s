BITS 32

extern printf
extern scanf

section .data
        fmt: db "%d",0
        sum: db "sum equals %d",10,0
        diff: db "difference equals  %d",10,0
        mul: db "product equals %d",10,0
        div: db "qoutient equals %d",10,0

section .text
        global main
        
        main:
        push ebp
        mov ebp,esp

        lea eax, [ebp-0x4]
        push eax
        push fmt
        call scanf

        lea edx, [ebp-0x8]
        push edx
        push fmt
        call scanf 
        
        mov ebx, dword [ebp-0x4]
        mov eax, dword [ebp-0x8]
        add eax, ebx

        push eax
        push sum
        call printf

        mov ebx, dword [ebp-0x4]
        mov eax, dword [ebp-0x8]
        sub ebx,eax

        push ebx
        push diff
        call printf

        mov ebx, dword [ebp-0x4]
        mov eax, dword [ebp-0x8]
        mul ebx
        
        push eax
        push mul
        call printf

        mov edx, 0
        mov eax, dword [ebp-0x4]
        mov ecx, dword [ebp-0x8]
        div ecx
        mov ebx, edx

        push eax
        push div
        call printf

        leave
        ret
