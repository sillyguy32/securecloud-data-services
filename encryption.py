from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
public_key = key.publickey()

cipher_encrypt = PKCS1_OAEP.new(public_key)
cipher_decrypt = PKCS1_OAEP.new(key)

def encrypt_data(data: str) -> bytes:
    return cipher_encrypt.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes) -> str:
    return cipher_decrypt.decrypt(encrypted_data).decode()