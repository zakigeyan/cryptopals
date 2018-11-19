BLOCK_SIZE = 20

def pad(s):
	return s + chr(BLOCK_SIZE - (len(s) % BLOCK_SIZE)) * (BLOCK_SIZE - (len(s) % BLOCK_SIZE))

a = raw_input()
print repr(pad(a))