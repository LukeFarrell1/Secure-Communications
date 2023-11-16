import hashlib
import sys
import binascii
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad  # Added import
import random

def encrypt(word, key, mode):
    plaintext = pad(word.encode(), AES.block_size)
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    rtn = encobj.decrypt(ciphertext)
    return unpad(rtn, AES.block_size).decode()

rnd = random.randint(1, 2**128)
keyA = hashlib.md5(str(rnd).encode()).digest()

rnd = random.randint(1, 2**128)
keyB = hashlib.md5(str(rnd).encode()).digest()

print('Long-term Key Alice=', binascii.hexlify(keyA).decode())
print('Long-term Key Bob=', binascii.hexlify(keyB).decode())

rnd = random.randint(1, 2**128)
keySession = hashlib.md5(str(rnd).encode()).hexdigest()

ya = encrypt(keySession, keyA, AES.MODE_ECB)
yb = encrypt(keySession, keyB, AES.MODE_ECB)

print("Encrypted key sent to Alice:", binascii.hexlify(ya).decode())
print("Encrypted key sent to Bob:", binascii.hexlify(yb).decode())

decipherA = decrypt(ya, keyA, AES.MODE_ECB)
decipherB = decrypt(yb, keyB, AES.MODE_ECB)

print("Session key:", decipherA)
print("Session key:", decipherB)