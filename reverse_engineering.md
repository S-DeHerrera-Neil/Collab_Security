# Static (look at the file)
- Determine file signatures
- String analysis (YARA)
# Behavioral (what does it do)
- Procmon (check system calls)
- autoruns (while it runs)
# Dynamic (debug it)
- x64_debugger or x32_debugger
# Disassembly (understand the code)
## Step 1. Follow strings found via string analysis
![image](https://github.com/user-attachments/assets/a7675c5e-ea3b-4a22-9fb1-7b239a1d4166)
In this example we found a string key and found where the string is located

By clicking on the reference in the assembly seem above, we can find the function and it's decompiled result:
![image](https://github.com/user-attachments/assets/a0b1c3fb-4650-4017-9558-3034d1fc0acb)
```
void FUN_00401040(void)

{
  FILE *pFVar1;
  int iVar2;
  char local_1c [20];
  uint local_8;
  
  local_8 = DAT_0041a02c ^ (uint)&stack0xfffffffc;
  FUN_00401130((wchar_t *)s_Enter_Key:_0041a000);
  pFVar1 = (FILE *)___acrt_iob_func(0);
  FUN_00403308(local_1c,0x14,pFVar1);
  _strtok(local_1c,&DAT_0041a00c);
  iVar2 = FUN_00401000(local_1c);
  if (iVar2 == 0x34f3) {
    FUN_00401130((wchar_t *)s_Success!!._0041a010);
    Sleep(5000);
  }
  else {
    FUN_00401130((wchar_t *)s_Failed!!._0041a01c);
    Sleep(5000);
  }
  FUN_0040116a(local_8 ^ (uint)&stack0xfffffffc);
  return;
```
This is very verbose so lets pick it apart

```
  if (iVar2 == 0x34f3) {
    FUN_00401130((wchar_t *)s_Success!!._0041a010);
```
This part of the code represents the success condition, which begs the question: how is iVar2 set?

```
iVar2 = FUN_00401000(local_1c);
```
This is set by a function "FUN_00401000"

Select the function and find the code:
```
undefined4 __cdecl FUN_00401000(char *param_1)

{
  int iVar1;
  undefined4 uVar2;
  
  iVar1 = FID_conflict:_atoi(param_1);
  if (iVar1 == 0x7b) {
    uVar2 = 0x34f3;
  }
  else {
    uVar2 = 0xc;
  }
  return uVar2;
}
```
param_1 effectively means user input

This script uses atoi to grab the first contiguous group of numbers which is set to iVar1

If the result is 0x7b then uVar2 is set to 0x34f3
otherwise uVar2 is set to 0xc

# Document Findings (REPORT)
