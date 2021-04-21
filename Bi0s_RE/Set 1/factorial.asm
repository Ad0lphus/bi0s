BITS 32
extern scanf
extern printf

section .rodata
	in: db "Enter N: ",0
	fmt: db "%d",0
	out: db "factorial is %d",20,0
section .text
	global main
	main:

	mov ebp,esp
	push ebp
	sub esp,0x12

	push in
	call printf
	lea eax,[ebp-0x4]
	push eax
	push fmt
	call scanf

	mov ecx,DWORD[ebp-0x4]

	LOOP:
	mov eax,DWORD[ebp-0x4]
	dec ecx

	mul ecx
	mov DWORD[ebp-0x4],eax
	
	cmp ecx,1
	je end

	jmp LOOP

	end:
	push DWORD[ebp-0x4]
	push out
	call printf
	ret
