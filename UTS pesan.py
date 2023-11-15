import base64

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def encrypt_and_encode(message, shift):
    encrypted_message = caesar_cipher_encrypt(message, shift)
    encoded_message = base64.b64encode(encrypted_message.encode()).decode()
    return encoded_message

# Contoh penggunaan
pesan = "Jangan lupa sholat dan selalu hormati orang tua anda"
pergeseran = 3
pesan_terenkripsi = encrypt_and_encode(pesan, pergeseran)
print("Pesan Terenkripsi:", pesan_terenkripsi)