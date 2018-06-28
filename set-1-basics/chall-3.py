import string

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

for key in range(0x00, 0xff):
	b = ''
	for j in a:
		b += chr(ord(j) ^ key)
	if all(c in string.printable for c in b):
		print b

# Cooking MC's like a pound of bacon
