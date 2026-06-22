from core.file_steganography import FileSteganography


def test_hide_and_extract_file_roundtrip(tmp_path):
    secret_path = tmp_path / "secret.txt"
    hidden_path = tmp_path / "hidden_file.png"
    extracted_dir = tmp_path / "out"

    original_content = b"Top secret bytes"
    secret_path.write_bytes(original_content)
    extracted_dir.mkdir()

    FileSteganography.hide_file(
        image_path="sample.png",
        file_path=str(secret_path),
        password="secure123",
        output_path=str(hidden_path),
    )

    extracted_file = FileSteganography.extract_file(
        image_path=str(hidden_path),
        password="secure123",
        output_directory=str(extracted_dir),
    )

    assert (extracted_dir / "secret.txt").exists()
    assert extracted_file.endswith("secret.txt")
    assert (extracted_dir / "secret.txt").read_bytes() == original_content