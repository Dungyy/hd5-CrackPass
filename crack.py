#!/usr/bin/env python3
# Disclaimer: This script is for educational purposes only.  Do not use against any network that you don't own or have authorization to test.

import hashlib 

#flag = 0
counter = 0

print(r'''
 _   _ ____  ____     ____                _         
| | | |  _ \| ___|   / ___|_ __ __ _  ___| | __ ____
| |_| | | | |___ \  | |   | '__/ _` |/ __| |/ /|_  /
|  _  | |_| |___) | | |___| | | (_| | (__|   <  / / 
|_| |_|____/|____/   \____|_|  \__,_|\___|_|\_\/___|            
''')
print("***********************************************")
print("* Twitter : https://twitter.com/CodeWithDungy *")
print("* GitHub : https://github.com/Dungyy          *")
print("***********************************************")
print("\n")
pass_hash = input("Enter md5 Hash: ")
wordList = input("File Name: ")
print("\n")
print(25 * "==")
print("\n")
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
        print("Password has been found!")
        print("\n")
        print("Password is ==> " + word)
        print(25 * "==")
        break 

#if flag == 0: 
#   print("Password is not in the list")   