# Creating Socket File
Creating Socket File for tunnel
```
ssh -MS /tmp/jump user@ip
```
Creating a tunnel through a forward
```
ssh -MS /tmp/t1 creds@127.0.0.1 -p 3333 
```
# Forward Through Socket File
```
ssh -S /tmp/jump random -O forward -L2222:192.168.28.100:80 -L3333:192.168.28.100:2222
```
# Setup and Teardown Proxychains
Run proxychain through socket file
```
ssh -S /tmp/jump random -O forward -D9050
```
Teardown proxychain
```
ssh -S /tmp/jump random -O cancel -D9050
```
