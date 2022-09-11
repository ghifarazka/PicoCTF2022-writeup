# find index from username
# find password using the same index
# decipher

# uname we want
username = "cultiris"

# open uname file
f = open("usernames.txt", "r")
f = f.read()

# separate by newline
f_list = f.split("\n")

# loop, find uname index/line number
for i in f_list:
	if i == username:
		global index
		index = f_list.index(i)

# open pass file
g = open("passwords.txt", "r")
g = g.read()

# separate by newline
g_list = g.split("\n")

# find pass of same index
for i in g_list:
	if g_list.index(i) == index:
		print(i)

# after this just decipher it as rot13