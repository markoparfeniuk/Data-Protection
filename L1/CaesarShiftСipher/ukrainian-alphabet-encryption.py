# Ukrainian alphabet
lowercase_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
uppercase_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

def shift_cipher_encrypt(text, shift):
    return ''.join([lowercase_alphabet[(lowercase_alphabet.index(c) + shift) % len(lowercase_alphabet)] if c in lowercase_alphabet
        else uppercase_alphabet[(uppercase_alphabet.index(c) + shift) % len(uppercase_alphabet)] if c in uppercase_alphabet
        else c for c in text])

def shift_cipher_decrypt(text, shift):
    return ''.join([lowercase_alphabet[(lowercase_alphabet.index(c) - shift) % len(lowercase_alphabet)] if c in lowercase_alphabet
        else uppercase_alphabet[(uppercase_alphabet.index(c) - shift) % len(uppercase_alphabet)] if c in uppercase_alphabet
        else c for c in text])


# Example
while True:
    text = input("Input text (>100 characters), letters only: ")  # text input
    if len(text) > 100 and all(c.lower() in lowercase_alphabet for c in text):
        break
    else:
        print("Invalid input. Please enter a text of length 100 or more and use letters only.")

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

# read encrypted text from вулиця (encrypted).txt
with open('вулиця (encrypted).txt', 'r', encoding='utf-8') as f:
    encrypted_text = f.read()

# decrypt encrypted text
decrypted_text = shift_cipher_decrypt(encrypted_text, shift)

print(decrypted_text)
