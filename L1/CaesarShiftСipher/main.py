# Ukrainian alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz .,'

def shift_cipher_encrypt(text, shift):
    return ''.join([alphabet[(alphabet.index(c) + shift) % len(alphabet)] if c in alphabet else c for c in text])

def shift_cipher_decrypt(text, shift):
    return ''.join([alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in text])


# Example
text = input("Input text (100 characters): ") # text input

# write text input into street.txt
with open('street.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# read text from street.txt
with open('street.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# encrypt text
shift = 24
encrypted_text = shift_cipher_encrypt(text, shift)

# write encrypted text into street (encrypted).txt
with open('street (encrypted).txt', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)

# read encrypted text from street (encrypted).txt
with open('street (encrypted).txt', 'r', encoding='utf-8') as f:
    encrypted_text = f.read()

# decrypt encrypted text
decrypted_text = shift_cipher_decrypt(encrypted_text, shift)

print(decrypted_text)