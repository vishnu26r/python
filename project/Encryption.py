import random
import string

chars =" " + string.whitespace + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)


# print(f" chars: {chars}")
# print(f" key: {key}")

#Encrypt

plain_text = input("Enter a message to encrypt ")
cipher_text = " " 
 
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#Decrypt

cipher_text= input("Enter a message to encrypt ")
plain_text= " " 
 
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
