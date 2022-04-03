# Sleuthkit Apprentice (200 Pts)

### Description
> Download this disk image and find the flag.

After extracting the disk image file, use `mmls` to know the offset of the bottom Linux (0x83) partition, which is `360448`.

```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```
Then, use the command `fls -o 360448 disk.flag.img` to open the partition. 
```
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 451:	home
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles

```
CTFs usually hide flag in the root folder, so go to root by using the command `fls -o 360448 disk.flag.img 1995`.
```
r/r 2363:	.ash_history
d/d 3981:	my_folder

```
Open my folder with `fls -o 360448 disk.flag.img 3981`.
```
r/r * 2082(realloc):	flag.txt
r/r 2371:	flag.uni.txt
```
Now use `icat -o 360448 disk.flag.img 2371` to read the flag file.

flag: `picoCTF{by73_5urf3r_152f373f}`