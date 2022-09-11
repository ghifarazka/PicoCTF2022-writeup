# diffie-hellman (200 Pts)

### Description
> Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message?

The message is `H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_7IGK58KC`. Using the diffie-hellman algorithm,
```
p = 13
g = 5

a = 7
b = 3

A = 5^7 mod 13 = 8
B = 5^3 mod 13 = 8

s = 8^7 mod 13  OR  s = 8^3 mod 13
s = 5
```
the secret is `5`. Now do Caesar shift by 5 to the message with the alphabet 0-9 + A-Z. Try shifting it forward and backward. Then put the decoded message in the flag format. 

Yes, this challenge is very brute-able. They even didn't put it on PicoGym after the event lol.

flag: `picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_2DBF03F7}`