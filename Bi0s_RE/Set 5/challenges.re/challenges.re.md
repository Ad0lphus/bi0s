# challenges.re

## 1) X86/X64 SSE   : 13,  15,  16,  20, 31

### Reverse Engineering Challenge #13

*Tags: .*

*What does this SSE code do?*

*Optimizing GCC 4.8.2:*


```asm
f:
	xor	rax, rax
.L4:
	movdqu	xmm0, XMMWORD PTR [rsi+rax]
	movdqu	xmm1, XMMWORD PTR [rdx+rax]
	pmaxub	xmm0, xmm1
	movdqu	XMMWORD PTR [rdi+rax], xmm0
	add	rax, 16
	cmp	rax, 1024
	jne	.L4
	rep ret


```

Solution:

>SSE stands for Streaming SIMD Extensions. It is essentially the floating-point equivalent of the MMX instructions. The SSE registers are 128 bits, and can be used to perform operations on a variety of data sizes and types. Unlike MMX, the SSE registers do not overlap with the floating point stack.[(source)](https://en.wikibooks.org/wiki/X86_Assembly/SSE)

Here, In this challenge they used two instructions namely movdqu and pmaxub.
movdqu - **Moves a double quadword** from the second operand to the first operand. This instruction can be used to load an XMM register from a 128-bit memory location, to store the contents of an XMM register into a 128-bit memory location.

here, 128 bit value is stored in xmm register.

**pmaxub - Maximum of Packed Unsigned Integers**

here, it returns the maximum of two values.

Therefore, the above set of instructions represents the algoritham for finding the maximum of two numbers.


---

### Reverse Engineering Challenge #15

*Tags: .
Now that's really easy. What does this code do?
Optimizing clang 3.4, LLVM 3.4, AT&T syntax:*

```asm
f:                                      # @f
        xorps   %xmm0, %xmm0
        movups  %xmm0, 240(%rdi)
        movups  %xmm0, 224(%rdi)
        movups  %xmm0, 208(%rdi)
        movups  %xmm0, 192(%rdi)
        movups  %xmm0, 176(%rdi)
        movups  %xmm0, 160(%rdi)
        movups  %xmm0, 144(%rdi)
        movups  %xmm0, 128(%rdi)
        movups  %xmm0, 112(%rdi)
        movups  %xmm0, 96(%rdi)
        movups  %xmm0, 80(%rdi)
        movups  %xmm0, 64(%rdi)
        movups  %xmm0, 48(%rdi)
        movups  %xmm0, 32(%rdi)
        movups  %xmm0, 16(%rdi)
        movups  %xmm0, (%rdi)
        ret
```

**Solution**

from the first instruction, ```xorps   %xmm0, %xmm0```, Its Xoring(XORPS — Bitwise Logical XOR of Packed Single Precision Floating-Point Values) xmm0 with itself ==> returning zero.

```MOVUPS — Move Unaligned Packed Single-Precision Floating-Point Values```

So basically all the `movups` instructions making everything zero from the buffer.



---


### Reverse Engineering challenge #20

*Tags: .*

*This is easy. What does the following code do?*

*Optimizing GCC 4.8.2 for x64*


```asm

f4:
.LFB40:
        sub     rsp, 8
        call    rand
        cvtsi2ss        xmm0, eax
        mulss   xmm0, DWORD PTR .LC0[rip]
        add     rsp, 8
        ret
.LC0:
        .long   805306368
```
As you may notice, it uses SSEx instructions for floating point number processing. The code below was compiled by the same version of GCC, but using -march=pentium3 -m32 switches, that forces it to compile code for 80x87 FPU:

```asm
f4:
        sub     esp, 28
        call    rand
        mov     DWORD PTR [esp+12], eax
        fild    DWORD PTR [esp+12]
        fmul    DWORD PTR .LC0
        add     esp, 28
        ret
.LC0:
        .long   805306368
```
Optimizing Keil 5.05 (ARM mode)
```asm
||f4|| PROC
        PUSH     {r4,lr}
        BL       rand
        BL       __aeabi_i2f
        POP      {r4,lr}
        MVN      r1,#0x1e
        B        __ARM_scalbnf
        ENDP
```

Optimizing Keil 5.05 (Thumb mode)
```asm
||f4|| PROC
        PUSH     {r4,lr}
        BL       rand
        BL       __aeabi_i2f
        MOVS     r1,#0x1e
        MVNS     r1,r1
        BL       __ARM_scalbnf
        POP      {r4,pc}
        ENDP
```
Optimizing GCC 4.9.3 for ARM64
```asm
f4:
        stp     x29, x30, [sp, -16]!
        add     x29, sp, 0
        bl      rand
        scvtf   s1, w0
        ldr     s0, .LC0
        ldp     x29, x30, [sp], 16
        fmul    s0, s1, s0
        ret
.LC0:
        .word   805306368
```

Optimizing GCC 4.4.5 for MIPS
```asm
f4:
        lui     $28,%hi(__gnu_local_gp)
        addiu   $sp,$sp,-32
        addiu   $28,$28,%lo(__gnu_local_gp)
        sw      $31,28($sp)
        lw      $25,%call16(rand)($28)
        nop
        jalr    $25
        nop

        mtc1    $2,$f0
        lui     $2,%hi($LC0)
        cvt.s.w $f2,$f0
        lw      $31,28($sp)
        lwc1    $f0,%lo($LC0)($2)
        addiu   $sp,$sp,32
        j       $31
        mul.s   $f0,$f2,$f0
$LC0:
        .word   805306368
```

**Solution**



```cvtsi2ss        xmm0, eax``` -> CVTSI2SS — Convert Doubleword Integer to Scalar Single-Precision Floating-Point Value.
and here we can see that it is calling a function ```rand()``` . 

So, according to that i guess that the function is returing the multiplicative value of a random floating point number between(0,1) and 805306368.



---

### Reverse Engineering challenge #31.
*Tags: .*

*What does this code do?*

*Optimizing MSVC 2010 x86*
```asm
__real@3fe0000000000000 DQ 03fe0000000000000r
__real@3f50624dd2f1a9fc DQ 03f50624dd2f1a9fcr

_g$ = 8
tv132 = 16
_x$ = 16
f1 PROC
	fld	QWORD PTR _x$[esp-4]
	fld	QWORD PTR __real@3f50624dd2f1a9fc
	fld	QWORD PTR __real@3fe0000000000000
	fld	QWORD PTR _g$[esp-4]
$LN2@f1:
	fld	ST(0)
	fmul	ST(0), ST(1)
	fsub	ST(0), ST(4)
	call	__ftol2_sse
	cdq
	xor	eax, edx
	sub	eax, edx
	mov	DWORD PTR tv132[esp-4], eax
	fild	DWORD PTR tv132[esp-4]
	fcomp	ST(3)
	fnstsw	ax
	test	ah, 5
	jnp	SHORT $LN19@f1
	fld	ST(3)
	fdiv	ST(0), ST(1)
	faddp	ST(1), ST(0)
	fmul	ST(0), ST(1)
	jmp	SHORT $LN2@f1
$LN19@f1:
	fstp	ST(3)
	fstp	ST(1)
	fstp	ST(0)
	ret	0
f1 ENDP

__real@3ff0000000000000 DQ 03ff0000000000000r

_x$ = 8
f2 PROC
	fld	QWORD PTR _x$[esp-4]
	sub	esp, 16
	fstp	QWORD PTR [esp+8]
	fld1
	fstp	QWORD PTR [esp]
	call	f1
	add	esp, 16
	ret	0
f2 ENDP
```
Optimizing MSVC 2012 x64
```asm
__real@3fe0000000000000 DQ 03fe0000000000000r
__real@3f50624dd2f1a9fc DQ 03f50624dd2f1a9fcr
__real@3ff0000000000000 DQ 03ff0000000000000r

x$ = 8
f	PROC
	movsdx	xmm2, QWORD PTR __real@3ff0000000000000
	movsdx	xmm5, QWORD PTR __real@3f50624dd2f1a9fc
	movsdx	xmm4, QWORD PTR __real@3fe0000000000000
	movapd	xmm3, xmm0
	npad	4
$LL4@f:
	movapd	xmm1, xmm2
	mulsd	xmm1, xmm2
	subsd	xmm1, xmm3
	cvttsd2si eax, xmm1
	cdq
	xor	eax, edx
	sub	eax, edx
	movd	xmm0, eax
	cvtdq2pd xmm0, xmm0
	comisd	xmm5, xmm0
	ja	SHORT $LN18@f
	movapd	xmm0, xmm3
	divsd	xmm0, xmm2
	addsd	xmm0, xmm2
	movapd	xmm2, xmm0
	mulsd	xmm2, xmm4
	jmp	SHORT $LL4@f
$LN18@f:
	movapd	xmm0, xmm2
	ret	0
f	ENDP
```

**Solution**

```asm
__real@3fe0000000000000 DQ 03fe0000000000000r
__real@3f50624dd2f1a9fc DQ 03f50624dd2f1a9fcr
__real@3ff0000000000000 DQ 03ff0000000000000r

x$ = 8
f	PROC
	movsdx	xmm2, QWORD PTR __real@3ff0000000000000
	movsdx	xmm5, QWORD PTR __real@3f50624dd2f1a9fc
	movsdx	xmm4, QWORD PTR __real@3fe0000000000000
	movapd	xmm3, xmm0
	npad	4
$LL4@f:
	movapd	xmm1, xmm2                #Move packed double-precision floating-point values from xmm2 to xmm1.
	mulsd	xmm1, xmm2                #Multiply the low double-precision floating-point value in xmm2 by low double-precision floating-point value in xmm1.
	subsd	xmm1, xmm3                #Subtract the low double-precision floating-point value in xmm3 from xmm1 and store the result in xmm1.
	cvttsd2si eax, xmm1               #Convert Scalar Double-Precision Floating-Point Value to Doubleword Integer
	cdq                               #Convert Word to Doubleword/Convert Doubleword to Quadword
	xor	eax, edx
	sub	eax, edx
	movd	xmm0, eax
	cvtdq2pd xmm0, xmm0               #Convert two packed signed doubleword integers from xmm0 to two packed double-precision floating-point values in xmm0.
	comisd	xmm5, xmm0                #Compare low double-precision floating-point values
	ja	SHORT $LN18@f
	movapd	xmm0, xmm3
	divsd	xmm0, xmm2
	addsd	xmm0, xmm2
	movapd	xmm2, xmm0
	mulsd	xmm2, xmm4
	jmp	SHORT $LL4@f
$LN18@f:
	movapd	xmm0, xmm2
	ret	0
f	ENDP
```

input1 from the user is subtracted from real@3fe0000000000000 and is converted to int datatype. similary from that input2 is subtracted and converted to floating point datatype. and it gets compared with __real@3f50624dd2f1a9fc using a loop. if the conditions becomes true then it does calculation using the constant values and returns the value when the loop exits.
---


## 2.ARM  : 2,  3 ,  4,  5 , 6

### Reverse Engineering challenge #2.
*Tags: .*

*What does this code do?*

*Optimizing GCC 4.8.2 -m32:*

```asm
<f>:
   0:          mov    eax,DWORD PTR [esp+0x4]
   4:          bswap  eax
   6:          mov    edx,eax
   8:          and    eax,0xf0f0f0f
   d:          and    edx,0xf0f0f0f0
  13:          shr    edx,0x4
  16:          shl    eax,0x4
  19:          or     eax,edx
  1b:          mov    edx,eax
  1d:          and    eax,0x33333333
  22:          and    edx,0xcccccccc
  28:          shr    edx,0x2
  2b:          shl    eax,0x2
  2e:          or     eax,edx
  30:          mov    edx,eax
  32:          and    eax,0x55555555
  37:          and    edx,0xaaaaaaaa
  3d:          add    eax,eax
  3f:          shr    edx,1
  41:          or     eax,edx
  43:          ret
  ```
  
**Solution :**

```    4:          bswap  eax``` =>BSWAP Instruction Swap Bytes(i.e. in reverse)
`shl` and ``shr`` instruction simply shifts the mentioned bits in the register to the left side or right side one by one

```asm
   6:          mov    edx,eax
   8:          and    eax,0xf0f0f0f
   d:          and    edx,0xf0f0f0f0
  13:          shr    edx,0x4
  16:          shl    eax,0x4
  19:          or     eax,edx
  ```
  
  so basically these set of instruction performs ``((var & 0xf0f0f0f) << 4) | ((var & 0xf0f0f0f0) >> 4)``


similarly , 
``((var & 0x33333333) << 2) | ((var & 0xcccccccc) >> 2)``
``  3d:          add    eax,eax`` ==> eax * 2
``((var & 0x55555555) << 1) | ((var & 0xaaaaaaaa) >> 1)``


To get the output i just wrote a simple C program with the observed statements-
```c=
#include <stdio.h>
int main(){
    for(int var=1;var<256;var++)
    {
        var=((var & 0xf0f0f0f) << 4) | ((var & 0xf0f0f0f0) >> 4);
        var=((var & 0x33333333) << 2) | ((var & 0xcccccccc) >> 2);
        var=((var & 0x55555555) << 1) | ((var & 0xaaaaaaaa) >> 1);
        printf("%u %x\n",var,var);
    }
}
```
Output:

![](https://i.imgur.com/4LYGtmb.png)



---

### Reverse Engineering challenge #3.
*Tags: .*

*What does this code do? The function has array of 64 32-bit integers, I removed it in each assembly code snippet to save space. The array is:*

```c
int v[64]=
	{ -1,31, 8,30, -1, 7,-1,-1, 29,-1,26, 6, -1,-1, 2,-1,
	  -1,28,-1,-1, -1,19,25,-1, 5,-1,17,-1, 23,14, 1,-1,
	   9,-1,-1,-1, 27,-1, 3,-1, -1,-1,20,-1, 18,24,15,10,
	  -1,-1, 4,-1, 21,-1,16,11, -1,22,-1,12, 13,-1, 0,-1 };
```
*The algorithm is well-known, but I've changed constant so it wouldn't be googleable.*

Optimizing GCC 4.8.2:

```asm
f:
	mov	edx, edi
	shr	edx
	or	edx, edi
	mov	eax, edx
	shr	eax, 2
	or	eax, edx
	mov	edx, eax
	shr	edx, 4
	or	edx, eax
	mov	eax, edx
	shr	eax, 8
	or	eax, edx
	mov	edx, eax
	shr	edx, 16
	or	edx, eax
	imul	eax, edx, 79355661 ; 0x4badf0d
	shr	eax, 26
	mov	eax, DWORD PTR v[0+rax*4]
	ret
```
**Solution:**
```asm
f:
	mov	edx, edi                       #n
	shr	edx                            #n >> 1
	or	edx, edi                       #n >> 1 | n
	mov	eax, edx                       # ==> va1=var2=n >> 1 | n
	shr	eax, 2                         #var1>>2
	or	eax, edx                       #var1>>2|var2
	mov	edx, eax                       # ==>var1=var2=var1>>2|var2
	shr	edx, 4                         #var2>>4
	or	edx, eax                       #var2>>4|var1
	mov	eax, edx                       # ==> var1=var2=var2>>4|var1
	shr	eax, 8                         #var1>>8
	or	eax, edx                       #var1>>8|var2
	mov	edx, eax                       # ==> var1=var2=var1>>8|var2
	shr	edx, 16                        #var2>>16
	or	edx, eax                       # ==> var2=var2>>16|var1
	imul	eax, edx, 79355661 ; 0x4badf0d #var2*0x4badf0d
	shr	eax, 26                        # ==>var1=var2*0x4badf0d>>26
	mov	eax, DWORD PTR v[0+rax*4]      
	ret                                #return v[var1]
```


when i convert this in C language the 
```c=
#include <stdio.h>
int main(){
    int v[64]=
	{ -1,31, 8,30, -1, 7,-1,-1, 29,-1,26, 6, -1,-1, 2,-1,
	  -1,28,-1,-1, -1,19,25,-1, 5,-1,17,-1, 23,14, 1,-1,
	   9,-1,-1,-1, 27,-1, 3,-1, -1,-1,20,-1, 18,24,15,10,
	  -1,-1, 4,-1, 21,-1,16,11, -1,22,-1,12, 13,-1, 0,-1 };
    unsigned var1,var2;

    for(int n=0;n<50;n++){
        var1=var2=n >> 1 | n;
        var1=var2=var1>>2|var2;
        var1=var2=var2>>4|var1;
        var1=var2=var1>>8|var2;
        var2=var2>>16|var1;
        var1=var2*0x4badf0d>>26;
        printf("%d\t",v[var1]);}
    printf("\n");
    return var1;
}
```
output:
![](https://i.imgur.com/9cnWAhu.png)

by looking at the output we can see a pattern of numbers;
```
31-0    (*1)
31-1    (*2)
31-2    (*4)
31-3    (*8) ...etc
```


---
### Reverse Engineering challenge #4.
*Tags: .*

*What does this code do?*

*Some versions have the 0x1010101 constant, some do not. Why?*

Optimizing GCC 4.8.2:

```asm
<f>:
   0:          mov    edx,edi
   2:          shr    edx,1
   4:          and    edx,0x55555555
   a:          sub    edi,edx
   c:          mov    eax,edi
   e:          shr    edi,0x2
  11:          and    eax,0x33333333
  16:          and    edi,0x33333333
  1c:          add    edi,eax
  1e:          mov    eax,edi
  20:          shr    eax,0x4
  23:          add    eax,edi
  25:          and    eax,0xf0f0f0f
  2a:          imul   eax,eax,0x1010101
  30:          shr    eax,0x18
  33:          ret
```

**Solution:**

```asm
<f>:
   0:          mov    edx,edi                #var
   2:          shr    edx,1                  #var >> 1
   4:          and    edx,0x55555555         #var >> 1 & 0x55555555
   a:          sub    edi,edx                # ==> var= var - var >> 1 & 0x55555555
   c:          mov    eax,edi                #var
   e:          shr    edi,0x2                #var >> 2
  11:          and    eax,0x33333333         #var & 0x33333333
  16:          and    edi,0x33333333         #var >> 2 & 0x33333333
  1c:          add    edi,eax                # ==> var=var >> 2 & 0x33333333+var & 0x33333333
  1e:          mov    eax,edi                #var
  20:          shr    eax,0x4                #var >>4
  23:          add    eax,edi                #var>>4+var
  25:          and    eax,0xf0f0f0f          #(var + (var >> 4)) & 0xf0f0f0f
  2a:          imul   eax,eax,0x1010101      #((var + (var >> 4)) & 0xf0f0f0f) * 0x1010101
  30:          shr    eax,0x18               # ==> ((var + (var >> 4)) & 0xf0f0f0f) * 0x1010101 >>0x18
  33:          ret                           #return
```

I converted the above infos to C program:

```c=
#include <stdio.h>
int main(int var)
{
    for(var=0;var<25;var++){
    int i=var;
    var= var - ((var >> 1) & 0x55555555);
    var = ((var >> 2) & 0x33333333) + (var & 0x33333333);
    var=((var + (var >> 4)) & 0xf0f0f0f) * 0x1010101 >> 0x18;
    printf("%d\t%d\n",i,var);var=i;}
    return var;
}
```

Output:
![](https://i.imgur.com/5o9IN2f.png)

but not able to figure out the algo -__-
and about ``0x1010101`` constant... idk exactly, may be it will use some other instruction or get derived from some other constant.. idk :/
---
### Reverse Engineering challenge #5.
*Tags: .*

*What does this code do?*

Optimizing GCC 4.8.4 (x64):

```asm
f:
	cmp	rcx, rsi
	ja	.L10
	sub	rsi, rcx
	add	rsi, 1
	mov	r11, rsi
	je	.L10
	test	rcx, rcx
	jne	.L16
	mov	rax, rdi
	ret
.L10:
	xor	eax, eax
	ret
.L16:
	push	rbx
	xor	r10d, r10d
	mov	r9d, 1
.L4:
	lea	rax, [rdi+r10]
	xor	esi, esi
	xor	r8d, r8d
.L8:
	movzx	ebx, BYTE PTR [rdx+rsi]
	cmp	BYTE PTR [rax+rsi], bl
	cmovne	r8d, r9d
	add	rsi, 1
	cmp	rsi, rcx
	jne	.L8
	test	r8d, r8d
	je	.L12
	add	r10, 1
	cmp	r10, r11
	jne	.L4
	xor	eax, eax
.L12:
	pop	rbx
	ret
```

**Solution:**

I've tried to depict the above situation in c language.

```c=
#include <stdio.h>
char main(char char1,char char2, unsigned num1,  unsigned num2)
{
    if (num1<=num2) {
        return 0;
    }
    num1=num1-num2+1;
    if (num1==0) {
        return 0;
    }
    if (num2==0) {
        return char1;
    }
    for (int i=0;i!=num1;i++)
    {
        unsigned flag=0;
        for (int j=0;j!=num2;j++) 
        {
            if (char1[i]!=char2[j]) 
            {
                flag=1;
            }
        }
        if (!flag) 
        {
            return char1+i;
        }
    }
    return 0;
}

```
### Reverse Engineering challenge #6.
*Tags:* .

*What does this code do? This is one of the simplest exercises I made, but still this code can be served as useful library function and is certainly used in many modern real-world applications.*

Non-optimizing GCC 4.8.2:

```asm
<f>:
   0:             push   rbp
   1:             mov    rbp,rsp
   4:             mov    QWORD PTR [rbp-0x8],rdi
   8:             mov    QWORD PTR [rbp-0x10],rsi
   c:             mov    rax,QWORD PTR [rbp-0x8]
  10:             movzx  eax,BYTE PTR [rax]
  13:             movsx  dx,al
  17:             mov    rax,QWORD PTR [rbp-0x10]
  1b:             mov    WORD PTR [rax],dx
  1e:             mov    rax,QWORD PTR [rbp-0x10]
  22:             movzx  eax,WORD PTR [rax]
  25:             test   ax,ax
  28:             jne    2c 
  2a:             jmp    38 
  2c:             add    QWORD PTR [rbp-0x8],0x1
  31:             add    QWORD PTR [rbp-0x10],0x2
  36:             jmp    c 
  38:             pop    rbp
  39:             ret
```

**Solution:**

it just copies the bytes when the comparison(if the charecter not equal to NULL) becomes true.

---
## 3. X86/X64 FPU  : 20 , 31 ,  36 , 60 ,  61

### Reverse Engineering challenge #36.
*Tags:* .

*A well-known algorithm again. What does it do? Also, take notice that the code for x86 uses FPU, but SIMD instructions are used instead in the x64 code. That's OK.*

Optimizing GCC 4.8.1 x86
```asm
f1:
	sub	esp, 4
	imul	eax, DWORD PTR v1.2023, 1664525
	add	eax, 1013904223
	mov	DWORD PTR v1.2023, eax
	and	eax, 8388607
	or	eax, 1073741824
	mov	DWORD PTR [esp], eax
	fld	DWORD PTR [esp]
	fsub	DWORD PTR .LC0
	add	esp, 4
	ret
f:
	push	esi
	mov	esi, 1000000
	push	ebx
	xor	ebx, ebx
	sub	esp, 16
.L7:
	call	f1
	fstp	DWORD PTR [esp]
	call	f1
	lea	eax, [ebx+1]
	fld	DWORD PTR [esp]
	fmul	st, st(0)
	fxch	st(1)
	fmul	st, st(0)
	faddp	st(1), st
	fld1
	fucomip	st, st(1)
	fstp	st(0)
	cmova	ebx, eax
	sub	esi, 1
	jne	.L7
	mov	DWORD PTR [esp+4], ebx
	fild	DWORD PTR [esp+4]
	fmul	DWORD PTR .LC3
	fdiv	DWORD PTR .LC4
	fstp	DWORD PTR [esp+8]
	fld	DWORD PTR [esp+8]
	add	esp, 16
	pop	ebx
	pop	esi
	ret

v1.2023:
	.long	305419896
.LC0:
	.long	1077936128
.LC3:
	.long	1082130432
.LC4:
	.long	1232348160
```
**Solution:**

```asm
f1:                                            #function f1
	sub	esp, 4
	imul	eax, DWORD PTR v1.2023, 1664525    #var * 1664525    (var = 305419896)
	add	eax, 1013904223                        #var * 1664525 + 1013904223
	mov	DWORD PTR v1.2023, eax                 # -> memmory
	and	eax, 8388607                           #((var * 1664525 + 1013904223) & 8388607)
	or	eax, 1073741824                        #((var * 1664525 + 1013904223) & 8388607) | 1073741824
	mov	DWORD PTR [esp], eax
	fld	DWORD PTR [esp]                        #Load Floating Point Value
	fsub	DWORD PTR .LC0                         #The FISUB instructions convert an integer source operand to double extended-precision floating-point format before performing the subtraction.
                                                      #(((var * 1664525 + 1013904223) & 8388607) | 1073741824) - 1077936128
	add	esp, 4
	ret
f:                                                    #function f
	push	esi
	mov	esi, 1000000
	push	ebx
	xor	ebx, ebx
	sub	esp, 16
.L7:
	call	f1                                     #var1 = f1()
	fstp	DWORD PTR [esp]
	call	f1                                     #var2 = f1()
	lea	eax, [ebx+1]
	fld	DWORD PTR [esp]
	fmul	st, st(0)                              #var1*2
	fxch	st(1)                                  #The fxch instruction exchanges the value on the top of stack with one of the other FPU registers
	fmul	st, st(0)                              #var2*2
	faddp	st(1), st                              #var1*2+var2*2
	fld1                                           #Push +1.0 onto the FPU register stack.
	fucomip	st, st(1)                              #Compare ST(0) with ST(i), check for ordered values, set status flags accordingly, and pop register stack.
	fstp	st(0)
	cmova	ebx, eax
	sub	esi, 1
	jne	.L7                                     # probably for loop
	mov	DWORD PTR [esp+4], ebx                      
	fild	DWORD PTR [esp+4]
	fmul	DWORD PTR .LC3
	fdiv	DWORD PTR .LC4
	fstp	DWORD PTR [esp+8]
	fld	DWORD PTR [esp+8]
	add	esp, 16
	pop	ebx
	pop	esi
	ret

v1.2023:
	.long	305419896
.LC0:
	.long	1077936128
.LC3:
	.long	1082130432
.LC4:
	.long	1232348160
```

there are few calculations which are done and it just returns a value after going through a loop and some conditions. 

---


### Reverse Engineering challenge #60.
*Tags: X86 L1 ASM FPU .*

This piece of code...

```c=
#include <stdio.h>

double d_max (double a, double b)
{
	if (a>b)
		return a;

	return b;
};

int main()
{
	// test
	printf ("%f\n", d_max (1.2, 3.4));
	printf ("%f\n", d_max (5.6, -4));
};
```
... is compiled by optimizing GCC 4.8.1 into the following piece of 32-bit x86 assembly code:

```asm
	fld	QWORD PTR [esp+4]
	fld	QWORD PTR [esp+12]
	fxch	st(1)
	fucomi	st, st(1)
	fcmovbe	st, st(1)
	fstp	st(1)
	ret
```
Try to eliminate the FXCH instruction, and test it.

**solution:**

```asm
	fld	QWORD PTR [esp+4]             #a
	fld	QWORD PTR [esp+12]            #b
	fxch	st(1)                     #st(1)=b and compare a and b
	fucomi	st, st(1)                 #move st1,b,to st0 if a<=b else as it is
	fcmovbe	st, st(1)                 #Move if below or equal
	fstp	st(1)
	ret
```
The fxch instruction exchanges the value on the top of stack with one of the other FPU registers.
a and b values are swapped after FXCH is executed. which will not be happend if se eliminate ``FXCH``.The last fstp leaves st(0) on top of stack discarding st(1)



---

### Reverse Engineering challenge #61.
*Tags: MIPS L1 ASM FPU ARM64 .*
*What does this code do?*

Optimizing GCC 4.9 (ARM64)
```asm
f:
	fadd	d0, d0, d1
	fmov	d1, 5.0e+0
	fadd	d2, d0, d2
	fadd	d3, d2, d3
	fadd	d0, d3, d4
	fdiv	d0, d0, d1
	ret
```
**Solution:**

```asm
f:
	fadd	d0, d0, d1
	fmov	d1, 5.0e+0            #5 is constant
	fadd	d2, d0, d2
	fadd	d3, d2, d3
	fadd	d0, d3, d4
	fdiv	d0, d0, d1            #divides with the constant 5
	ret
```

code in c:
```c=
#include <stdio.h>
float main()
{
    float var1,var2,var3,var4,var5;
    return (var1+var2+var3+var4+var5)/5;
}
```