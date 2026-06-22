from PIL import Image


class LSBDecoder:

    HEADER_SIZE = 32

    @staticmethod
    def decode(image_path):

        image = Image.open(
            image_path
        )

        image = image.convert(
            "RGB"
        )

        pixels = list(
            image.getdata()
        )

        bits = []

        for pixel in pixels:

            r, g, b = pixel

            bits.append(
                str(r & 1)
            )

            bits.append(
                str(g & 1)
            )

            bits.append(
                str(b & 1)
            )

        bits = ''.join(bits)

        payload_length = int(
            bits[:32],
            2
        )

        start = 32

        end = (
            start +
            payload_length * 8
        )

        payload_bits = bits[
            start:end
        ]

        data = bytearray()

        for i in range(
            0,
            len(payload_bits),
            8
        ):

            byte = payload_bits[
                i:i + 8
            ]

            data.append(
                int(byte, 2)
            )

        return bytes(data)