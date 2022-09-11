# basic-mod1 (100 Pts)

### Description
> We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Hints
- Do you know what mod 37 means?
- mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

Take each number from message.txt and do "[number] mod 37" on each. Then for each remainder decrypt it according to the instructions. To make it easier, I made a python script `solve.py`.

flag: `picoCTF{R0UND_N_R0UND_C0A86577}`