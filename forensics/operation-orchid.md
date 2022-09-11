# Operation Orchid (400 Pts)

### Description
> Download this disk image and find the flag.

As usual, open the disk image file, use `mmls` to know the partition offset, navigate to root folder. Here's what we have in the root folder:
```
r/r 1875:	.ash_history
r/r * 1876(realloc):	flag.txt
r/r 1782:	flag.txt.enc
```
`*` means "deleted" here, so I tried to recover "flag.txt" using `tsk_recover -o 411648 -d 472 disk.flag.img .` ["411648" is the partition offset, "472" is the directory inumeration for the root folder, "." means "output the file(s) in current directory"] and got the "flag.txt" file recovered. Using `cat` on it, I got: 
```
           -0.881573            34.311733
```
Which looked like a coordinate. Searching it on Maps, the place is in the middle of nowhere and provided us no clue [I later figured why this way doesn't work].

Alternatively, using `cat` on "flag.txt.enc" reveals:
```
Salted__���3[u
              :dmޠ
D-Z{z�+g�p�=�N���\��B�Ȥ7� ���؎$�'%
```
Now, the problem is decrypting. I got stuck here. I tried searching for the "key" in different folders but found nothing. Then, I tried to do `strings disk.flag.img | grep [keyword]` with keywords such as "pico", "flag", and then I tried "flag.txt". It shows:
```
$ strings disk.flag.img | grep flag.txt 
flag.txt
flag.txt.enc
touch flag.txt
nano flag.txt 
nano flag.txt 
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
flag.txt
flag.txt
flag.txt.enc
flag.txt
flag.txt.enc
```
Very nice. Now we just need to put the message in "flag.txt.enc" into a file called "file.txt" and then run the decryption command. Here are the commands I used.

Putting the message to file: `icat -o 411648 disk.flag.img 1782 > file.txt`

Decrypting the message: `openssl aes256 -d -salt -in file.txt -out flag.txt -k unbreakablepassword1234567`

Using `cat` on "flag.txt", we get the flag.

flag: `picoCTF{h4un71ng_p457_c512004e}`

P.S. We can see above that the flagmaker used `shred -u flag.txt`. According to Wikipedia, *shred is a command on Unix-like operating systems that can be used to securely delete files and devices so that it is extremely difficult to recover them, even with specialized hardware and technology; assuming it's even possible to recover the file at all. It is a part of GNU Core Utilities.* I think this is why recovering the file with `tsk_recover` earlier didn't work.