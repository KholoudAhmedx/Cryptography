
alphabet = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Read the key & plaintext values
Plaintext = input("Enter the plaintext: ")

while True:
    Key = input("Enter the key value: ")
    if len(Key) < len(Plaintext) or len(Key) == len(Plaintext):
        break
    print("Length of the key must be less than or equal the plaintext, please enter the value again.")

key = Key.upper()
plaintext = Plaintext.upper()

# # If plaintext has a letter J convert it to I
new_plaintext = plaintext.replace('J', 'I')
#print("Plaintext is :", new_plaintext)


rearranged_alphabet = []
seen = set()

# Add key to the 5x5 matrix
for i in range(len(key)):
    if key[i] not in seen:
        seen.add(key[i])    
        rearranged_alphabet.append(key[i])
#print(rearranged_alphabet)

# Add the rest of the alphabets to the 5x5 matrix
for i in range(len(alphabet)):
    if alphabet[i] not in rearranged_alphabet and alphabet[i] != 'J':
        rearranged_alphabet.append(alphabet[i])
#print(rearranged_alphabet)

# Convert the list to 2D array 
num_columns = 5
num_rows = 5
for i in range(0, len(rearranged_alphabet), 5):
    rearranged_alphabet_2D =[rearranged_alphabet[i*num_columns:(i+1)*num_columns] for i in range(num_rows)]

#print(rearranged_alphabet_2D)


plaintext_pairs = []
plaintext_notrepeated = ""

for i in range(len(new_plaintext)-1):
    if new_plaintext[i] == new_plaintext[i+1]:
        plaintext_notrepeated+=new_plaintext[i]
        plaintext_notrepeated+='X'
    else:
        plaintext_notrepeated+=new_plaintext[i]
# Add the last character separately
plaintext_notrepeated += new_plaintext[-1]

# When plaintext is odd
if len(plaintext_notrepeated) % 2 != 0:
    plaintext_notrepeated+='Z'
    
#print(new_plaintext)
#print("Plaintext without repeat: ", plaintext_notrepeated)

for i in range(0,len(plaintext_notrepeated), 2):
    current_slice = plaintext_notrepeated[i: i+2]
    plaintext_pairs.append(current_slice)
#print("List of pairs are:", plaintext_pairs)

# Encryption
cipher = ""
for i in range(len(plaintext_pairs)):
    a = plaintext_pairs[i][0]
    b = plaintext_pairs[i][1]
    for j in range(num_rows):
        for k in range(num_columns):
            if a == rearranged_alphabet_2D[j][k]:
                a_row = j
                a_column = k
            elif b == rearranged_alphabet_2D[j][k]:
                b_row = j
                b_column = k
    if a_row == b_row:
        cipher+= rearranged_alphabet_2D[a_row][(a_column + 1)%5]
        cipher+= rearranged_alphabet_2D[b_row][(b_column + 1)%5]
    elif a_column == b_column:
        cipher+= rearranged_alphabet_2D[(a_row + 1)%5][a_column]
        cipher+= rearranged_alphabet_2D[(b_row + 1)%5][b_column]
    else:
        cipher+= rearranged_alphabet_2D[a_row][b_column%5]
        cipher+= rearranged_alphabet_2D[b_row][a_column%5]
print("Ciphertext is: ", cipher.lower())

