# Ukrainian alphabet
alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

def shift_cipher_encode(text, shift):
    return ''.join([alphabet[(alphabet.index(c) + shift) % len(alphabet)] if c in alphabet else c for c in text])

def shift_cipher_decode(text, shift):
    return ''.join([alphabet[(alphabet.index(c) - shift) % len(alphabet)] if c in alphabet else c for c in text])

# Test case
text = 'привіт'
shift = 3

encoded = shift_cipher_encode(text, shift)
print(f'Encrypted text: {encoded}')

decoded = shift_cipher_decode(encoded, shift)
print(f'Decrypted text: {decoded}')