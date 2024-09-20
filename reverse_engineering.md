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
Note: x86_64 can operate with 64, 32, or 16 bit registries with the appending of:
```

```


| Register | Description |
| - | - |
| `%rax` | the first return register |
| `%rbp` | the base pointer that keeps track of the base of the stack |
| `%rsp` | the stack pointer that points to the top of the stack |

|Register |Accumulator| Base | Counter |Stack Pointer | Stack Base Pointer |Destination |Source |Data|
| - | - | - | - | - | - | - | - | - |
|64-bit |RAX 	|RBX 	|RCX 	|RSP 	|RBP 	|RDI 	|RSI 	|RDX|
|32-bit |EAX 	|EBX 	|ECX 	|ESP 	|EBP 	|EDI 	|ESI 	|EDX|
|16-bit |AX 	|BX 	|CX 	|SP 	|BP 	|DI 	|SI 	|DX|

## Instructions

## 


	

the first return register

%rbp
	

the base pointer that keeps track of the base of the stack

%rsp
	

the stack pointer that points to the top of the stack
