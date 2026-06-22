from PIL import Image
import math


class ImageMetrics:

    @staticmethod
    def calculate_mse(
        original_path,
        stego_path
    ):

        original = Image.open(
            original_path
        ).convert("RGB")

        stego = Image.open(
            stego_path
        ).convert("RGB")

        original_pixels = list(
            original.getdata()
        )

        stego_pixels = list(
            stego.getdata()
        )

        mse = 0

        total_values = (
            len(original_pixels) * 3
        )

        for p1, p2 in zip(
            original_pixels,
            stego_pixels
        ):

            for c1, c2 in zip(
                p1,
                p2
            ):

                mse += (
                    c1 - c2
                ) ** 2

        mse /= total_values

        return mse

    @staticmethod
    def calculate_psnr(
        original_path,
        stego_path
    ):

        mse = ImageMetrics.calculate_mse(
            original_path,
            stego_path
        )

        if mse == 0:
            return float('inf')

        psnr = 20 * math.log10(
            255 / math.sqrt(mse)
        )

        return psnr