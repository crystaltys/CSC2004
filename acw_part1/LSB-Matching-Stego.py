#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

import sys
from cv2 import cv2
import numpy as np
import random

def extract():
    J=cv2.imread('test.png')
    f = open('output_payload.txt', 'w+', errors="ignore")
    idx=0
    bitidx=0
    bitval=0
    #print("Jshape",J.shape[0])
    for i in range(J.shape[0]): # height of the image 
        if (I[i, 0, 0] == '-'): 
            break
        for j in range(J.shape[1]): # width of the image
            for k in range(3):
                if (I[i, j, k] == '-'):
                    break
                if bitidx==8 and idx<=len(blist):
                    f.write(chr(bitval))
                    bitidx=0
                    bitval=0
                    idx+=1
                bitval |= (I[i, j, k]%2)<<bitidx
                bitidx+=1


    f.close()


bits=[]
f=open('payload2.txt', 'r') # patload2.tx contains string of texts.
blist = [ord(b) for b in f.read()]  # ord() function convert each char to ASCII code. Payload character value
for b in blist:
    for i in range(8): 
        bits.append((b >> i) & 1) 

I = np.asarray(cv2.imread('C:\\Users\\tyscr\\Desktop\\Steganography\\test.png')) # convert image to numpy array
# I is a numpy array with height x width x 3(RGB) contains cover image pixel values
sign=[1,-1]
idx=0
# the code below encodes the payload into the image
for i in range(I.shape[0]): # image height
    for j in range(I.shape[1]): # image width 
        for k in range(3): 
            if idx<len(bits): # bits array has 150 char x 8 bits = 1200 bits
                if I[i][j][k]%2 != bits[idx]: # +1 or -1 randomly if the LSB pixel value does not match the payload pixel value (from MSB)
                    s=sign[random.randint(0, 1)]
                    if I[i][j][k]==0: s=1 
                    if I[i][j][k]==255: s=-1
                    I[i][j][k]+=s 
                idx+=1

cv2.imwrite('test.png', I)

print("Extracting ... ")
extract()
print("Completed")