import numpy as np
import math 


alphabet = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Prompt the user for plaintext & key
Plaintext = input("Enter the plaintext: ")
while True:
    Key = input("Enter the key: ")
    if len(Key) < len(Plaintext) or len(Key) == len(Plaintext):
        break
    print("You must enter a key that is equal to or less than the length of the plaintex, try again.")

# print(Plaintext.upper(), "\n")
# print(Key.upper())

# To match with the alphabet
key = Key.upper()
plaintext = Plaintext.upper()


Key_pos = []
for i in range(len(key)):
    for a in range(len(alphabet)):
        if key[i] == alphabet[a]:
            Key_pos.append(a)
            break
p_pos = [] 
for k in range(len(plaintext)):
    for j in range(len(alphabet)):
        if plaintext[k] == alphabet[j]:
            p_pos.append(j)
            break
# print(Key_pos)
# print(p_pos)

cipher_pos = []
for i in range(0, len(p_pos), len(Key_pos)):
    current_slice = p_pos[i:i+len(Key_pos)]

    for j in range(len(Key_pos)):
        new_pos = (current_slice[j] + Key_pos[j]) % 26
        #print(new_pos)
        cipher_pos.append(new_pos)

# print(cipher_pos)

cipher_text = ""
# Generate cipher
for i in range(len(cipher_pos)):
    for j in range(len(alphabet)):
        if cipher_pos[i] == j:
            cipher_text+=alphabet[j]
print("Ciphertext is: ",cipher_text)
