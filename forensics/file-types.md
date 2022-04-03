# File types (100 Pts)

### Description
> This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

### Hints
- Remember that some file types can contain and nest other files.

We were given a file with a `.pdf` extension. After checking it with `file` and doing `cat` to the file, I found out that it's a bash script. Then, do as the comments told.

From this,
```sh
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00048
# Made on 2022-03-15 06:50 UTC by <root@ffe9b79d238c>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
````

to this, then save it in a file called `FILE`. 
```sh
'sh FILE'#!/bin/sh

# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00048
# Made on 2022-03-15 06:50 UTC by <root@ffe9b79d238c>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
```
If it raises an error about `uudecode`, install it first by using `sudo apt-get install sharutils`. After running `FILE`, we get the "flag" file, but it's actually an "ar archive file". So, decompress it. It then outputs the "flag" file but with another compression method, and so on. This is the order of the file types I had to go through: 

`ar > cpio > bzip2 > gzip > lzip > LZ4 > LZMA > lzop > lzip > XZ > ASCII`

In the end, we finally get the actual flag file. The flag was decoded in hex.

`7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33343765616536357d0a`

Decoding it, we get the flag.

flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_347eae65}`