from core.aes_crypto import CryptoManager
from core.lsb_encoder import LSBEncoder
from core.lsb_decoder import LSBDecoder
from core.file_handler import FileHandler
from core.integrity import IntegrityChecker

import os


class FileSteganography:

    SEPARATOR = b"::FILENAME::"
    HASH_SEPARATOR = b"::HASH::"

    @staticmethod
    def hide_file(
        image_path,
        file_path,
        password,
        output_path
    ):

        file_data = FileHandler.read_file(
            file_path
        )

        filename = os.path.basename(
            file_path
        ).encode()

        file_hash = (
            IntegrityChecker
            .generate_hash(file_data)
            .encode()
        )

        payload = (
            filename
            + FileSteganography.SEPARATOR
            + file_hash
            + FileSteganography.HASH_SEPARATOR
            + file_data
        )

        encrypted = CryptoManager.encrypt(
            payload,
            password
        )

        LSBEncoder.encode(
            image_path,
            encrypted,
            output_path
        )

        return output_path

    @staticmethod
    def extract_file(
        image_path,
        password,
        output_directory="."
    ):

        encrypted = LSBDecoder.decode(
            image_path
        )

        payload = CryptoManager.decrypt(
            encrypted,
            password
        )

        filename_part, remaining = (
            payload.split(
                FileSteganography.SEPARATOR,
                1
            )
        )

        hash_part, file_data = (
            remaining.split(
                FileSteganography.HASH_SEPARATOR,
                1
            )
        )

        filename = (
            filename_part.decode()
        )

        expected_hash = (
            hash_part.decode()
        )

        if not IntegrityChecker.verify_hash(
            file_data,
            expected_hash
        ):
            raise ValueError(
                "File integrity check failed"
            )

        output_file = os.path.join(
            output_directory,
            filename
        )

        FileHandler.write_file(
            output_file,
            file_data
        )

        return output_file