# This is for solving mod 37

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

	# mod 37 all
	mod = i % 37

	# if 0-25, it's uppercase alphabet
	if mod < 26:
		mod += 65
		msg += chr(mod)

	# if 26-35, it's number 0-9
	elif 25 < mod < 36:
		mod -= 26
		msg += str(mod)

	# if 36, it's underscore
	elif mod == 36:
		msg += "_"


print('picoCTF{' + msg + '}')
