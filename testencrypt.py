import hc128
import codecs

# Define the key and IV
key = "0F62B5085BAE0154A7FA4DA0F34699EC"
IV = "288FF65DC42B92F960C72E95FC63CA31"

print("Initializing HC-128 cipher state")
print("Key =", key)
print("IV =", IV)

# Initialize the HC-128 cipher with the key and IV
hc128.init(key, IV)

print("\nHC-128 Cipher state initialized")

# Get the plain text to encrypt from the user
plain_text = input("\nEnter plain text(in hex bytes, 4 at a time) to encrypt: ")

print("\nGenerating keystream, 4 bytes at a time")

# Generate the keystream
k = hc128.keygen()
print("Keystream generated: " + k)

# Convert the plain text and keystream from hex to bytes
plain_text = codecs.decode(plain_text, "hex")
k = codecs.decode(k, "hex")

# Initialize the cipher text as an empty byte string
cipher_text = b""

# XOR each byte of the plain text with the corresponding byte of the keystream to encrypt it
for i in range(0, 4):
    cipher_text += bytes([plain_text[i] ^ k[i]])

# Convert the cipher text from bytes to hex
cipher_text = codecs.encode(cipher_text, "hex")

# Print the encrypted cipher text
print("Encrypted cipher text: " + cipher_text.decode())