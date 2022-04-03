# SideChannel (400 Pts)

### Description
> There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? Download the PIN checker program here __pin_checker__. Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using `nc saturn.picoctf.net 50562` and provide it the PIN to get your flag.

### Hints
- Read about "timing-based side-channel attacks."
- Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it
- Don't run your attacks against the master server, it is secured against them. The PIN code you get from the `pin_checker` binary is the same as the one for the master server.

Firstly, make `pin_checker` executable using `chmod +x pin_checker`. Then try to put in PINs and check the execution time with the command `time -p ./pin_checker`. Since the program tells that it would be an 8-digit PIN, I tried to put in 00000000, 10000000, 20000000, and so on until 90000000. The execution time differs significantly when the input is "40000000". Here, pay attention to the "user" time.
```
$ time -p ./pin_checker 
Please enter your 8-digit PIN code:
30000000
8
Checking PIN...
Access denied.
real 4,87
user 0,31
sys 0,00
$ time -p ./pin_checker 
Please enter your 8-digit PIN code:
40000000
8
Checking PIN...
Access denied.
real 4,24
user 0,53
sys 0,02
$ time -p ./pin_checker 
Please enter your 8-digit PIN code:
50000000
8
Checking PIN...
Access denied.
real 5,49
user 0,30
sys 0,00
$ time -p ./pin_checker 
Please enter your 8-digit PIN code:
60000000
8
Checking PIN...
Access denied.
real 4,53
user 0,29
sys 0,01
```
The program processed the input PIN such that the more correct digit it has, the longer the program takes to check the PIN.

After this, I tried putting in 40000000, 41000000, 42000000, and so on until 49000000 and checking which one takes significantly longer time. I do this for every digit until I get the full PIN. The correct PIN is `48390513`. Use the PIN to access the master server and we get the flag.

flag: `picoCTF{t1m1ng_4tt4ck_8d0e5357}`