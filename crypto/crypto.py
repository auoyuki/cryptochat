from cryptography.fernet import Fernet

def generate_key():
    with open("secret.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(message.encode())

def decrypt_message(token: bytes, key: bytes) -> str:
    return Fernet(key).decrypt(token).decode()
