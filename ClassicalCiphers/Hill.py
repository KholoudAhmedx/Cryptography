import numpy as np 


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


plaintext = input("Enter plaintext please: ")

# Key must be an m x m matrix
# key is entered as a string for example key is : ciphering & then we convert it to mxm matrix 
m = int(input("Enter m where m is the size of the matrix: "))
while True:
    key = input("Enter the key: ").upper()
    if(len(key) == (m * m)):
        break;

key_list = []

# Get positions of key 
for i in range(len(key)):
    for j in range(len(alphabet)):
        if(key[i] == alphabet[j]):
            key_list.append(j)
print(key_list)

# Convert key list to matrix mxm
for i in range(0,len(key_list) ,m):
    key_matrix = [key_list[i * m : (i + 1)* m] for i in range(m)]
print(key_matrix)
def encrypt(k, p):

    return 0

