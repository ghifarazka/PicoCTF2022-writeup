# credstuff (100 Pts)

### Description
> We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? Download the leak here. The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

### Hints
- Maybe other passwords will have hints about the leak?

To find the password I made a Python script `solve.py`. Ctrl+F would've been faster, though. After getting the password, decipher it as ROT13 (It's hinted by another password in the same file)

flag: `picoCTF{C7r1F_54V35_71M3}`