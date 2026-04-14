from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

key = RSA.generate(2048)
public_key = key.publickey()

cipher_encrypt = PKCS1_OAEP.new(public_key)
cipher_decrypt = PKCS1_OAEP.new(key)


def encrypt_data(data: str) -> str:
    """
    Encrypt string → return BASE64 string
    """
    encrypted_bytes = cipher_encrypt.encrypt(data.encode())
    return base64.b64encode(encrypted_bytes).decode()


def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypt BASE64 string → return original string
    """
    encrypted_bytes = base64.b64decode(encrypted_data.encode())
    return cipher_decrypt.decrypt(encrypted_bytes).decode()
