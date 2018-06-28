import base64

a = open('6.txt').read().split()
a = ''.join(a)
b = base64.b64decode(a)
key = 'Terminator X: Bring the noise'
c = ''

for i in range(len(b)):
	c += chr(ord(b[i]) ^ ord(key[i % len(key)]))

print key
print c
