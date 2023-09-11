# Ukrainian alphabet
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def shift_cipher_encode(text, shift):
    return ''.join([alphabet[(alphabet.index(c) + shift) % len(alphabet)] if c in alphabet else c for c in text])

def shift_cipher_decode(text, shift):
    return ''.join([alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in text])


# Example
text = input("Input text (100 characters, letters only): ") # text input

# write text input into the file вулиця.txt
with open('вулиця.txt', 'w', encoding='utf-8') as f:
    f.write(text)