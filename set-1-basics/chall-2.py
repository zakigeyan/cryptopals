a = '1c0111001f010100061a024b53535009181c'.decode('hex')
b = '686974207468652062756c6c277320657965'.decode('hex')
c = ''

for i in range(len(a)):
	c += chr(ord(a[i]) ^ ord(b[i]))

print c
c = c.encode('hex')
print c

# the kid don't play
