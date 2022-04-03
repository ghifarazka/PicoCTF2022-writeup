# St3go (300 Pts)

### Description
Download this image and find the flag.

### Hints
- We know the end sequence of the message will be `$t3g0`.

To solve challenges like this, the key is to use the right stegangraphy tool. A list of tools like [this](https://0xrick.github.io/lists/stego) is very helpful. I tried using `stegsolve` on the image but I can't found the flag. Then I tried using `zsteg` and got the flag. 

```
$ zsteg pico.flag.png 
b1,r,lsb,xy         .. text: "~__B>+g?G@"
b1,g,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 3549684369
b1,g,msb,xy         .. file: dBase III DBT, version number 0, next free block index 3418965897
b1,b,lsb,xy         .. file: dBase III DBT, version number 0, next free block index 2623130757
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_1b8d71db}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b3,b,msb,xy         .. file: StarOffice Gallery theme @\002 H\200\004H\002\004H\200$H\022\004H\200\004\010, 0 objects
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,lsb,xy      .. file: Novell LANalyzer capture file
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
b4,abgr,lsb,xy      .. file: Novell LANalyzer capture file
```

flag: `picoCTF{7h3r3_15_n0_5p00n_1b8d71db}`