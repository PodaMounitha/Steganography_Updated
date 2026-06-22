from core.metrics import ImageMetrics
from core.lsb_encoder import LSBEncoder


def test_metrics_for_encoded_image(tmp_path):
    output_path = tmp_path / "hidden_file.png"
    LSBEncoder.encode("sample.png", b"metric-check", str(output_path))

    mse = ImageMetrics.calculate_mse("sample.png", str(output_path))
    psnr = ImageMetrics.calculate_psnr("sample.png", str(output_path))

    assert mse >= 0
    assert psnr > 0