#!/usr/bin/python
import sys
import re
import string

# ORIGINAL
def encrypt(plaintext, key):
    """Encrypt a plaintext using key.
    This method will return the ciphertext as a list of bytes.
    """
    ciphertext = []
    key_length = len(key)
    for i in range(len(plaintext)):
        p = ord(plaintext[i])
        k = ord(key[i % key_length])
        c = (p + k) % 256
        print("c is: ",c)
        ciphertext.append(c)
    return bytes(ciphertext)

def decrypt(ciphertext, key):
    """Dccrypt a ciphertext using key.
    This method will return the plaintext as a list of bytes.
    """
    plaintext = []
    key_length = len(key)
    for i in range(len(ciphertext)):
        p = ord(ciphertext[i])
        k = ord(key[i % key_length])
        c = (p - k) % 256
        plaintext.append(c)
    return bytes(plaintext)


# # TEST CODE
# # This function generates the 
# # key in a cyclic manner if 
# # it's length isn't equal to 
# # the length of original text 
# def generateKey(string, key): 
# 	key = list(key) 
# 	if len(string) == len(key): 
# 		return(key) 
# 	else: 
# 		for i in range(len(string) -
# 					len(key)): 
# 			key.append(key[i % len(key)]) 
# 	return("" . join(key)) 
	
# # This function returns the 
# # encrypted text generated 
# # with the help of the key 
# def encrypt(string, key): 
# 	print("Plaintext as string: ",string) 
# 	cipher_text = [] 
# 	for i in range(len(string)): 
# 		newChar = (ord(string[i]) +
# 			ord(key[i])) % 26 + 1
# 		# newChar += ord('A') 
# 		cipher_text.append(newChar) 
# 	print("cyphertext in num: ",cipher_text)
# 	return("bytes: ",bytes(cipher_text))
	
# # This function decrypts the 
# # encrypted text and returns 
# # the original text 

# # DOESN'T TAKE IN BYTES. If taking in POSITIONAL NUMBERS, IT WORKS. Basically CIPHERTEXT before the bytes(cipher_text)
# def decrypt(cipher_text, key): 
# 	orig_text = [] 
# 	for i in range(len(cipher_text)): 
# 		x = (cipher_text[i] - ord(key[i]) + 13) % 26
# 		x  = chr(64+x) 
# 		orig_text.append(x)
    
# 	orig_text=("" . join(orig_text))
# 	return(orig_text) 
	
# # Driver code 
# if __name__ == "__main__": 
# 	string = "HELLO"
# 	keyword = "ALICE"
# 	key = generateKey(string, keyword) 
# 	cipher_text = encrypt(string,key) 
# 	print("Ciphertext in num:", cipher_text) 
# 	print("Original/Decrypted Text :", 
# 		decrypt(cipher_text, key)) 

