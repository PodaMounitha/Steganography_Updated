from core.capacity_checker import CapacityChecker


def test_capacity_is_positive_for_sample_image():
    assert CapacityChecker.max_bytes("sample.png") > 0


def test_can_store_small_payload_in_sample_image():
    assert CapacityChecker.can_store("sample.png", 16)


def test_cannot_store_huge_payload_in_sample_image():
    assert not CapacityChecker.can_store("sample.png", 10**9)