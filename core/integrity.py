import hashlib


class IntegrityChecker:

    @staticmethod
    def generate_hash(data: bytes):

        return hashlib.sha256(
            data
        ).hexdigest()

    @staticmethod
    def verify_hash(
        data: bytes,
        expected_hash: str
    ):

        current_hash = hashlib.sha256(
            data
        ).hexdigest()

        return (
            current_hash
            == expected_hash
        )