# basic-mod2 (100 Pts)

### Description
> A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

### Hints
- Do you know what the modular inverse is?
- The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
- It's recommended to use a tool to find the modular inverses

The instructions are pretty clear already. To solve this, I made a Python script `solve.py` utilizing the mod inverse function made by ofaurax [here](https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49).

flag: `picoCTF{1NV3R53LY_H4RD_261CB530}`
