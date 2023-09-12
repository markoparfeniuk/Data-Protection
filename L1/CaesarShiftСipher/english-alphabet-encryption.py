# English alphabet
lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz .,'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,'

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
    text = input("Input text (>100 characters): ") # text input
    if len(text) > 100:
        break
    else:
        print("Text is too short. Please enter a text of length 100 or more.")

# write text input into street.txt
with open('street.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# read text from street.txt
with open('street.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# encrypt text
shift = 1
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
