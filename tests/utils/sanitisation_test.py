import pytest
from src.utils.sanitisation import Sanitisation


def test_sanitise():
    file = "Hello, World! Testing 123"
    expected_result = ["hello", "world", "testing", "123"]
    assert Sanitisation.sanitise(file) == expected_result


def test_sanitise_empty_file():
    file = ""
    expected_result = []
    assert Sanitisation.sanitise(file) == expected_result


def test_sanitise_special_characters():
    file = "!@#$% ^&*()"
    expected_result = []
    assert Sanitisation.sanitise(file) == expected_result


def test_sanitise_mixed_characters():
    file = "Hello, World! 123 Testing!"
    expected_result = ["hello", "world", "123", "testing"]
    assert Sanitisation.sanitise(file) == expected_result
