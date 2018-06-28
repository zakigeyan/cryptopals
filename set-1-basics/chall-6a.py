import base64

a = open('6.txt').read().split()
a = ''.join(a)
b = base64.b64decode(a)
print b

# $ python Chall_6.py > no6.txt
# $ xortool no6.txt -l 29 -c 20
# key = 'Terminator X: Bring the noise'
