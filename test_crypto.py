import pytest

from core.aes_crypto import CryptoManager


def test_encrypt_decrypt_roundtrip():
    message = b"Hello Fidelity"
    password = "secure123"

    encrypted = CryptoManager.encrypt(message, password)
    decrypted = CryptoManager.decrypt(encrypted, password)

    assert decrypted == message


def test_decrypt_with_wrong_password_fails():
    encrypted = CryptoManager.encrypt(b"secret", "correct-password")

    with pytest.raises(Exception):
        CryptoManager.decrypt(encrypted, "wrong-password")