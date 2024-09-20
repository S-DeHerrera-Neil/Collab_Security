# Pseudo Code
```
main:
	mov rax, 16 	// move 16 into rax registry
	push rax 	// push 16 to the stack
	jmp mem2 	// jump unconditional to function "mem2"

mem1:
	mov rax, 8 	// move 8 to rax register
	ret 		// return value of first return register (rax)

mem2:
	pop r8 		// remove top off stack (8 bytes) to register r8
	cmp rax, r8 	// compaer value of rax (16) to the value of r8 (16) they are equal
	je mem1 	// jump on equal to function mem1
```
# HELLO WORLD
Example C code:
```
#include<stdio.h>

int main(){
	printf("Hello World\n");
	return 0;
}
```
Converted Assembly Code
```
	.file	"test.c"
	.text
	.section	.rodata
.LC0:
	.string	"Hello World"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```
