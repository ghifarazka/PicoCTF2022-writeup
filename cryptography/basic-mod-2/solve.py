# This is for solving mod 37

# from ofaurax/modinverse.py
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

# open and read file (as string)
f = open("message.txt","r")
f = f.read()

# split by space
chars = f.split(" ")

# make them integers
chars_int = []
for i in chars:
	chars_int.append(int(i))

msg = ""

for i in chars_int:

	# take the mod inverse of each character and 41
	mod = modinv(i, 41)

	# if 1-26, it's uppercase alphabet
	if 0 < mod < 27:
		mod += 64
		msg += chr(mod)

	# if 27-36, it's number 0-9
	elif 26 < mod < 37:
		mod -= 27
		msg += str(mod)

	# if 37, it's underscore
	elif mod == 37:
		msg += "_"


print('picoCTF{' + msg + '}')
