#!/usr/bin/env python

from Crypto.Cipher import AES
import binascii, sys, string

teks = open('10.txt').read()
teks = teks.replace('\n', '')
teks = teks.decode('base64')

KEY="YELLOW SUBMARINE"
IV="\x00"*16

def encrypt(message,passphrase):
	aes = AES.new(passphrase,AES.MODE_CBC,IV)
	return aes.encrypt(message)

def decrypt(message,passphrase):
	aes = AES.new(passphrase,AES.MODE_CBC,IV)
	return aes.decrypt(message)

a = decrypt(teks,KEY)
print a