#!/usr/bin/env python3.6

#################  tested with python 3.6 x86 on Win 10 home using text files  ###########################################

print ("***by Jonesy167 https://github.com/Jonesy167***")
print ("")
print ("this program will encrypt and decrypt data within text files using a user password")
#import modules
import os
import sys
import pathlib
import binascii
import subprocess
import warnings


print ("")
print ("")
print ("")

task1 = input ("Press 1 to encrypt, press 2 to decrypt       ")

if task1 in ["1"]:
    import encrypt
elif task1 in ["2"]:
    import decrypt

while task1 not in range(1, 2):
    task1 = input("Press 1 to encrypt, press 2 to decrypt       ")
    if task1 in ["1"]:
        import encrypt
    elif task1 in ["2"]:
        import decrypt
