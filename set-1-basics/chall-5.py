a = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
b = ""

for i in range(len(a)):
	b += chr(ord(a[i]) ^ ord(key[i % len(key)]))

print b.encode('hex')
