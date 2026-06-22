from core.steganography import SecureSteganography


def test_secure_steganography_roundtrip(tmp_path):
    output_path = tmp_path / "secured.png"
    message = "Fidelity International 2027"

    SecureSteganography.hide_message(
        image_path="sample.png",
        message=message,
        password="secret123",
        output_path=str(output_path),
    )

    recovered = SecureSteganography.reveal_message(
        image_path=str(output_path),
        password="secret123",
    )

    assert recovered == message