import hc128
import codecs

key = "0F62B5085BAE0154A7FA4DA0F34699EC"
IV = "288FF65DC42B92F960C72E95FC63CA31"

print("Initializing HC-128 cipher state")
print("Key =", key)
print("IV =", IV)

hc128.init(key, IV)

print("\nHC-128 Cipher state initialized")

cipher_text = input("\nEnter cipher text(in hex bytes, 4 at a time) to decrypt: ")

print("\nGenerating keystream, 4 bytes at a time")
k = hc128.keygen()
print("Keystream generated: " + k)

cipher_text = codecs.decode(cipher_text, "hex")
k = codecs.decode(k, "hex")
plain_text = b""

for i in range(0, 4):
    plain_text += bytes([cipher_text[i] ^ k[i]])

plain_text = codecs.encode(plain_text, "hex")

print("Decrypted plain text: " + plain_text.decode())