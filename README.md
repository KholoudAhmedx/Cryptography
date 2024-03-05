# Objective
Implementing encryption algorithms including classical ciphers such as Caesar, Vigenere, Playfair and more,and modern ciphers such as AES,RC4..etc.

## Classical Ciphers
<ol><li>Caesar Cipher</li>
<li> Vigenere Cipher</li>
<li> Playfair Cipher </li>
<li> Hill Cipher: is a multi-letter substitution cipher based on linear algebra. </li></ol>

## How Each Algorithm Works
### Hill Cipher 
#### Encryption low is : 
<span style = "Bold" >C = E(K, P) mod 26 </span> <br />
Each letter is represented by a number modolu 26. <br /> 
Since hill cipher is a multi-letter algorithm, it means that it can encrpyt more than one letter at a time based on the size of the given key. <br \> 
The key is a n X n matrix that is multiplied by the plaintext to get the cipher text. The formula is as the following : <br /> ![image](https://github.com/KholoudAhmedx/Cryptography/assets/81588748/f10a9c0f-2c16-4819-958c-64dc5b80bc59)

If the key is given as a stirng, it is converted to the corresponding n X n matrix to multiply it to the plaintext. <br />
For example: if we have ```
Key = ciphering ``` then the corresponding matrix is 3x3 since the length of the key is 9 characters ![image](https://github.com/KholoudAhmedx/Cryptography/assets/81588748/e222c180-94fd-46cf-b7c9-118534c58496)

Hill cipher can encrypt a group of letters based on the size of the key matrix, so if we have a 3x3 key matrix then we can encrypt 3-plaintext letters at a time, if the key matrix is 2x2 matrix then 2-plaintext letters can be encrypted at a time and so on.. <br />
For example: ``` plaintext = "pay more money" and the 
key is 3x3 matrix, then we will encrypt the plaintext 3-letters at a time which means that we have p1 = pay, p2 = mor , p3= emo, p4 = ney and for each 3 letters. C1 = K x P1 mod 26 , c2 = K x P2 mod 26 and so on..``` <br />
Insert the letter 'x' to the plaintext if the last substring is less than the key length. 

