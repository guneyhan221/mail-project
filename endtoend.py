import hashlib

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Örnek kullanım
def password_hash(text):
    hashed_text = text
    for i in range(10000):
        hashed_text = hash_string(hashed_text)
    print(f"Hash: {hashed_text}")
    with open("hp.txt","a") as file:
        file.write(hashed_text)


