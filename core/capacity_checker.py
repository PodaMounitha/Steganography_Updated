from PIL import Image


class CapacityChecker:

    @staticmethod
    def max_bytes(image_path):

        image = Image.open(image_path)

        width, height = image.size

        total_bits = width * height * 3

        return total_bits // 8

    @staticmethod
    def can_store(
        image_path,
        payload_size
    ):

        return payload_size < CapacityChecker.max_bytes(
            image_path
        )