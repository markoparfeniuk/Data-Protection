# Ukrainian alphabet
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def shift_cipher_encrypt(text, shift):
    return ''.join([alphabet[(alphabet.index(c) + shift) % len(alphabet)] if c in alphabet else c for c in text])

def shift_cipher_decrypt(text, shift):
    return ''.join([alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in text])


# Example
text = input("Input text (100 characters, letters only): ") # text input

# write text input into вулиця.txt
with open('вулиця.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# read text from вулиця.txt
with open('вулиця.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# encrypt text
shift = 24
encrypted_text = shift_cipher_encrypt(text, shift)

# write encrypted text into вулиця (encrypted).txt
with open('вулиця (encrypted).txt', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)
