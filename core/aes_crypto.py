import os
import base64

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class CryptoManager:

    ITERATIONS = 100000

    @staticmethod
    def derive_key(password: str, salt: bytes):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=CryptoManager.ITERATIONS,
        )

        return kdf.derive(password.encode())

    @staticmethod
    def encrypt(data: bytes, password: str):

        salt = os.urandom(16)

        key = CryptoManager.derive_key(password, salt)

        aes = AESGCM(key)

        nonce = os.urandom(12)

        ciphertext = aes.encrypt(
            nonce,
            data,
            None
        )

        payload = salt + nonce + ciphertext

        return base64.b64encode(payload)

    @staticmethod
    def decrypt(payload: bytes, password: str):

        raw = base64.b64decode(payload)

        salt = raw[:16]
        nonce = raw[16:28]
        ciphertext = raw[28:]

        key = CryptoManager.derive_key(password, salt)

        aes = AESGCM(key)

        return aes.decrypt(
            nonce,
            ciphertext,
            None
        )