#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

import sys
from cv2 import cv2
import numpy as np
import random

# the code extracts the secret payload from the stego image
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
# opens file containing secret payload (string) data type and converts each char into ASCII code then (binary) 
# ord() function convert each char in secret payload to ASCII code  
f=open('payload2.txt', 'r') 
blist = [ord(b) for b in f.read()] 
for b in blist:
    for i in range(8): 
        bits.append((b >> i) & 1) 

# I is a numpy array with height x width x 3(RGB) contains cover image pixel values
# converts image to numpy array
I = np.asarray(cv2.imread('C:\\Users\\tyscr\\Desktop\\Steganography\\test.png')) 

sign=[1,-1]
idx=0
# payload hiding: the code below encodes the payload into the image
for i in range(I.shape[0]): # image height
    for j in range(I.shape[1]): # image width 
        for k in range(3): 
            if idx<len(bits): # bits array has 150 char x 8 bits = 1200 bits
                if I[i][j][k]%2 != bits[idx]: # if pixel binary is even, when mod 2=0 . When odd, =1. Only has to +1/-1 when pixel binary (LSB) is different from secret payload
