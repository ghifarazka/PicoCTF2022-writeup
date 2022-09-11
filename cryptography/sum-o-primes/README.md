# Sum-O-Primes (400 Pts)

### Description
> We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

### Hints
- I love squares :)

We are given the source code and the output file. From looking at the code, we can see that `n = pq` and `x = p+q`. Since `phi = (p-1)*(q-1)`, expand that to `phi = pq - (p + q) + 1`, we can conclude that `phi = n - x +1`. From there we can get the flag. Full solver is on `solver.py`.

flag: `picoCTF{ee326097}`