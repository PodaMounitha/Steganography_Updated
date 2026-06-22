from PIL import Image
from core.capacity_checker import CapacityChecker


class LSBEncoder:

    HEADER_SIZE = 32

    @staticmethod
    def bytes_to_binary(data: bytes):

        return ''.join(
            format(byte, '08b')
            for byte in data
        )

    @staticmethod
    def encode(
        image_path,
        payload: bytes,
        output_path
    ):

        image = Image.open(image_path)

        image = image.convert("RGB")

        payload_length = len(payload)

        header = format(
            payload_length,
            '032b'
        )

        binary_payload = (
            header +
            LSBEncoder.bytes_to_binary(
                payload
            )
        )

        required_bytes = (
            len(binary_payload) // 8
        ) + 1

        if not CapacityChecker.can_store(
            image_path,
            required_bytes
        ):
            raise ValueError(
                "Payload too large"
            )

        pixels = list(
            image.getdata()
        )

        data_index = 0

        new_pixels = []

        for pixel in pixels:

            rgb = list(pixel)

            for i in range(3):

                if data_index < len(
                    binary_payload
                ):

                    rgb[i] = (
                        rgb[i] & 254
                    ) | int(
                        binary_payload[
                            data_index
                        ]
                    )

                    data_index += 1

            new_pixels.append(
                tuple(rgb)
            )

        encoded = Image.new(
            image.mode,
            image.size
        )

        encoded.putdata(
            new_pixels
        )

        encoded.save(
            output_path
        )

        return output_path