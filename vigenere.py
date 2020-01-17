from cs50 import get_string
import sys

if len(sys.argv) != 2 or not sys.argv[1].isalpha():
    sys.exit("Invalid command line argument")

key = sys.argv[1]
key = key.lower()
convertKey = [ord(c) - 97 for c in key]

plainText = get_string("plaintext: ")
cipheredText = [None] * len(plainText)
keyStatus = 0
for c in range(len(plainText)):
    if plainText[c].isupper():
        cipheredText[c] = chr((ord(plainText[c]) - 65 + convertKey[keyStatus]) % 26 + 65)
        keyStatus += 1
        keyStatus %= len(key)

    elif plainText[c].islower():
        cipheredText[c] = chr((ord(plainText[c]) - 97 + convertKey[keyStatus]) % 26 + 97)
        keyStatus += 1
        keyStatus %= len(key)

    else:
        cipheredText[c] = plainText[c]
cipheredText = ''.join(cipheredText)
print ("ciphertext: " + cipheredText)