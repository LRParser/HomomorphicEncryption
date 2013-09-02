# Step 1: pick an n
n = 6

# Step 2: pick an odd integer > 2n for p

p = 27

# Step 3: pick an x in range -n/2,n/2

x = 2

# Pick k from 'some range'

k = 3

def encrypt(bit) :
    return bit + 2*x + k*p

def decrypt(num) :
    return (num % p) % 2

plainText1 = 0
encrypted1 = encrypt(plainText1)
decrypted1 = decrypt(encrypted1)

plainText2 = 1
encrypted2 = encrypt(plainText2)
decrypted2 = decrypt(encrypted2)

print "Plaintext1 is %d, encrypted1 is %d, decrypted1 is %d" % (plainText1, encrypted1, decrypted1)

print "Plaintext2 is %d, encrypted2 is %d, decrypted2 is %d" % (plainText2, encrypted2, decrypted2)

encryptedSum = encrypted1 + encrypted2
decryptedSum = decrypt(encryptedSum)

print "Encrypted sum is %d, decrypted sum is: %d" % (encryptedSum, decryptedSum)

encryptedProduct = encrypted1 * encrypted2
decryptedProduct = decrypt(encryptedProduct)

print "Encrypted product is %d, decrypted product is: %d" % (encryptedProduct, decryptedProduct)

