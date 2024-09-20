# [x86_64 Architecture](https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture)

## Terms
| Name | Description |
| - | - |
|Heap|Memory that can be allocated and deallocated|
|Stack|A contiguous section of memory used for passing arguments|
|General Register|A multipurpose register that can be used by either programmer or user to store data or a memory location address|
|Control Register|A processor register that changes or controls the behavior of a CPU|
|Flags Register|Contains the current state of the processor|
## Registers
Note: x86_64 can operate with 64, 32, or 16 bit registries

|Register |Accumulator| Base | Counter |Stack Pointer | Stack Base Pointer |Destination |Source |Data|
| - | - | - | - | - | - | - | - | - |
|64-bit |`RAX` 	|`RBX` 		|`RCX` 		|`RSP` 	|`RBP`	|`RDI` 	|`RSI` 	|`RDX`|
|32-bit |`EAX` 	|`EBX` 		|`ECX` 		|`ESP` 	|`EBP` 	|`EDI` 	|`ESI` 	|`EDX`|
|16-bit |`AX`	|`BX` 		|`CX` 		|`SP` 	|`BP` 	|`DI` 	|`SI` 	|`DX`|
|8-bit	|`AH`/`AL`|`BH`/`BL`	|`CH`/`CL`	|`SPL`  |`BPL`	| `SIL` | `DH`,`DL`|

| Register 		| 64-bit | 32-bit | 16-bit | 8-bit | Definition |
| - | - | - | - | - | - |
|Accumulator		|`RAX`|`EAX`|`AX`|`AH`/`AL`|
|Base			|`RBX`|`EBX`|`BX`|`BH`/`BL`|
|Counter		|`RCX`|`ECX`|`CX`|`CH`/`CL`|
|Stack Pointer		|`RSP`|`ESP`|`SP`|`SPL`|
|Stack Base Pointer	|`RBP`|`EBP`|`BP`|`BPL`|
|Destination		|`RDI`|`EDI`|`DI`|``|
|Source			|`RSI`|`ESI`|`SI`|`SIL`|
|Data			|`RDX`|`EDX`|`DX`|`DH`/`DL`|


## Instructions
| Operation | Description |
| - | - |
|MOV|move source to destination|
|PUSH|push source onto stack|
|POP|Pop top of stack to destination|
|INC|Increment source by 1|
|DEC|Decrement source by 1|
|ADD|Add source to destination|
|SUB|Subtract source from destination|
|CMP|Compare 2 values by subtracting them and setting the %RFLAGS register. ZeroFlag set means they are the same.|
|JMP|Jump to specified location|
|JLE|Jump if less than or equal|
|JE|Jump if equal|

## 


	

the first return register

%rbp
	

the base pointer that keeps track of the base of the stack

%rsp
	

the stack pointer that points to the top of the stack
