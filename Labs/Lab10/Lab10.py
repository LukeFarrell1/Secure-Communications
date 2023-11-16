from Crypto.PublicKey import RSA

key = RSA.generate(2048)

binPrivKey = key.export_key('DER')
binPubKey = key.publickey().export_key('PEM')

print(binPrivKey)
print(binPubKey)