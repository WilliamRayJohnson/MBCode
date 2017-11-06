'''
An Example of iterating a nonce in a hashing algorithm's input
Found in Mastering Bitcoin, Example 10-8
Adapted to work in python 3
'''

import hashlib

text = "I am Satoshi Nakamoto"

# iterate nonce from 0 to 19
for nonce in range(20):
    #add the nonce to the end of the text
    input = text + str(nonce)
    #calculate the SHA-256 hash of the input (text+nonce)
    hash = hashlib.sha256()
    hash.update(str.encode(input))
    hex = hash.hexdigest()
    #show the input and hash result
    print(input + ' => ' + hex)