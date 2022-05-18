#!/usr/bin/env python3
# Disclaimer: This script is for educational purposes only.  Do not use against any network that you don't own or have authorization to test.

import hashlib 

flag = 0
counter = 0

pass_hash = input("Enter md5 Hash: ")

wordList = input("File Name: ")

try: 
    pass_file = open(wordList, 'r')
except:
        print("No File found ")
        quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

# Show Live Feed of password cracking
    # print(word)
    # print(digest)
    # print(pass_hash)
    
    counter += 1

    if digest == pass_hash:
        print("Password has been found ")
        print("Password is " + word)
        break 

if flag == 0: 
    print("Password is not in the list")   