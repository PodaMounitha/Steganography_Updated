from core.aes_crypto import CryptoManager
from core.lsb_encoder import LSBEncoder
from core.lsb_decoder import LSBDecoder


class SecureSteganography:

    @staticmethod
    def hide_message(
        image_path,
        message,
        password,
        output_path
    ):

        encrypted = CryptoManager.encrypt(
            message.encode(),
            password
        )

        LSBEncoder.encode(
            image_path,
            encrypted,
            output_path
        )

        return output_path

    @staticmethod
    def reveal_message(
        image_path,
        password
    ):

        encrypted = LSBDecoder.decode(
            image_path
        )

        decrypted = CryptoManager.decrypt(
            encrypted,
            password
        )

        return decrypted.decode()