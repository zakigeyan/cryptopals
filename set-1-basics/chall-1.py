import base64

a = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'.decode('hex')
b = base64.b64encode(a)
print a
print b

# I'm killing your brain like a poisonous mushroom
