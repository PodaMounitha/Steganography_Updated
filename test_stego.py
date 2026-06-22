from core.lsb_encoder import LSBEncoder
from core.lsb_decoder import LSBDecoder


def test_lsb_encode_decode_roundtrip(tmp_path):
    message = b"Hello World"
    output_path = tmp_path / "encoded.png"

    LSBEncoder.encode("sample.png", message, str(output_path))
    result = LSBDecoder.decode(str(output_path))

    assert result == message