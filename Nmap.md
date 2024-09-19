# Nmap syntax
```
nmap [options] X.X.X.X/X -p X-XX,XXX --script=<script_1>: <script_2>: <script_3>
```
## Ping Sweep Types
| Switch | Name | Description |
| - | - | - |
| `-PS` | TCP SYN Ping | |
| `-PA` | TCP ACK Ping | |
| `-PU` | UDP Ping | |
| `-PE`, `-PP`, `-PM` | ICMP Ping | |

## [Port Scan Types](https://nmap.org/book/port-scanning-options.html)
| Switch | Name | Description |
| - | - | - |
| `-sS` | TCP SYN (Stealth) Scan | half connect scan (syn >, < syn/ack, rst >), requires sudo |
| `-sT` | TCP Connect Scan | full connect scan (syn >, < syn/ack, ack >, rst >) |
| `-sU` | UDP scan |
| `-sF` | TCP FIN scan |
| `-sN` | TCP NULL scan |
| `-sX` | TCP XMAS scan |

## Useful Options


# Using Scripts
## File location
```
/usr/share/nmap/scripts
```
## Syntax
```
nmap [options] [ip] --script=<script_1>: <script_2>: <script_3>
```
