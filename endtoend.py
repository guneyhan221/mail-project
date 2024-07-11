import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Örnek kullanım
def password_hash(text):
    hashed_text = text
    for i in range(10000):
        hashed_text = hash_string(hashed_text)
    #!print(f"Hash: {hashed_text}") test code
    return hashed_text

def encrypt_message(message, key):
    # AES için 16, 24 veya 32 bayt uzunluğunda bir anahtar gerekir

    # 16 baytlık bir IV (Initialization Vector) oluşturuyoruz
    iv = os.urandom(16)

    # AES algoritması ve CBC modu ile bir şifreleme nesnesi oluşturuyoruz
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Mesajı 16 baytlık bloklarla hizalamamız gerekiyor
    pad = 16 - len(message) % 16
    message += bytes([pad] * pad)

    # Mesajı şifreliyoruz
    ciphertext = encryptor.update(message) + encryptor.finalize()

    return iv + ciphertext

def decrypt_message(ciphertext, key):
    # İlk 16 baytlık kısmı IV olarak alıyoruz
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # AES algoritması ve CBC modu ile bir şifre çözme nesnesi oluşturuyoruz
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Şifrelenmiş metni çözüyoruz
    decrypted_message = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Padding'i kaldırıyoruz
    pad = decrypted_message[-1]
    decrypted_message = decrypted_message[:-pad]

    return decrypted_message

# Kendi belirlediğiniz anahtarı burada ayarlayın (16, 24 veya 32 bayt uzunluğunda olmalı)
# key = b'buanahtarbenwwww'  # 16 baytlık bir anahtar örneği

# # Şifrelenecek mesaj
# plaintext = b"Bu metin sifrelenecek."

# # Mesajı şifreleme
# ciphertext = encrypt_message(plaintext, key)
# print("Şifrelenmiş metin:", ciphertext)

# # Mesajı çözme
# decrypted_message = decrypt_message(ciphertext, key)
# print("Çözülmüş metin:", decrypted_message)
