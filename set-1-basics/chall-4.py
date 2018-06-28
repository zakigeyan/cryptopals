import string

aa = open('4.txt').read().split()
sp = string.printable

for a in aa:
	a = a.decode('hex')
	for key in range(0x00, 0xff):
		b = ''
		for j in a:
			b += chr(ord(j) ^ key)
		if all(c in sp for c in b):
			print b

# Now that the party is jumping
