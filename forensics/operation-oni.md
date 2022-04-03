# Operation Oni (300 Pts)

### Description
> Download this disk image, find the key and log into the remote machine. Remote machine: ssh -i key_file -p 57355 ctf-player@saturn.picoctf.net

After extracting the disk image, use `mmls` to know the offset of interest partition, in this case it's 206848. 
```
mmls disk.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```
Now open the partition using `fls -o 206848 disk.img`.
```
d/d 11:	lost+found
d/d 12:	boot
d/d 13:	etc
d/d 79:	proc
d/d 80:	dev
d/d 81:	tmp
d/d 82:	lib
d/d 85:	var
d/d 94:	usr
d/d 104:	bin
d/d 118:	sbin
d/d 458:	home
d/d 464:	media
d/d 468:	mnt
d/d 469:	opt
d/d 470:	root
d/d 471:	run
d/d 473:	srv
d/d 474:	sys
V/V 33049:	$OrphanFiles
```
CTFs usually hide flag in the root folder, so navigate to root folder using `fls -o 206848 disk.img 470`.

```
r/r 2344:	.ash_history
d/d 3916:	.ssh
```
Navigate to the `.ssh` directory using `fls -o 206848 disk.img 3916`.
```
r/r 2345:	id_ed25519
r/r 2346:	id_ed25519.pub
```
Now `icat` the file without the `.pub` extension, which holds the **private** key.
```
$ icat -o 206848 disk.img 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```
Then copy the inside and save it locally with the same file name. After that, use the provided command to log into the remote machine  `ssh -i id_ed25519 -p 57355 ctf-player@saturn.picoctf.net` (note: the port number might be different in different instances).

If there's an error saying that "keys are to open..." or something like that, use `chmod 400 file_name` to make it only readable by the user/owner.

After successfully logged in, use `ls` command. It shows that there's a `flag.txt`. `cat` it, and then we get the flag.

flag: `picoCTF{k3y_5l3u7h_dc01cec5}`