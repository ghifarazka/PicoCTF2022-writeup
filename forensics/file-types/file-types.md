# File Types

### Description
> 

We were given a file with a `.pdf` extension. After checking it with `file` and doing `cat` to the file, we found out that it's a bash script. Doing as the comments told (and after installing uudecodes in order for it to work), then runing the script, we get the "flag" file. The "flag" file is ending in `.ar`, so decompress it using such. It then outputs the file with another compression method, and so on. This is the order of the file types we had to go through: 

`ar > cpio > bzip2 > gzip > lzip > LZ4 > LZMA > lzop > lzip > XZ > ASCII`

In the end, we finally get the actual flag file. The flag was decoded in hex.

`7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33343765616536357d0a`

Decoding it, we get the flag.

flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_347eae65}`