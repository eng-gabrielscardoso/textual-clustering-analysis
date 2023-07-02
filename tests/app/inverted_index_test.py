import os
import pytest

from src.app.inverted_index import InvertedIndex
from src.utils.sanitisation import Sanitisation


@pytest.fixture
def inverted_index():
    files = []
    full_path = os.path.abspath("./src/assets/texts")
    for filename in os.listdir(full_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(full_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                sanitised_content = Sanitisation.sanitise(content)
                files.append(sanitised_content)

    return InvertedIndex(files)


def test_build(inverted_index):
    result1 = inverted_index.find("greenberg")
    result2 = inverted_index.find("abstract")
    assert result1["count"] == 1
    assert result2["count"] == 36


def test_find_existing_word(inverted_index):
    result1 = inverted_index.find("greenberg")
    result2 = inverted_index.find("abstract")
    assert result1["count"] == 1
    assert result2["count"] == 36


def test_find_non_existent_word(inverted_index):
    result1 = inverted_index.find("apple")
    result2 = inverted_index.find("abstract")
    assert result1 == {}
    assert not result2 == {}


def test_remove_existing_word(inverted_index):
    assert inverted_index.remove("greenberg")
    assert inverted_index.find("greenberg") == {}


def test_remove_non_existent_word(inverted_index):
    assert not inverted_index.remove("apple")


def test_clear_index(inverted_index):
    assert inverted_index.clear()
    assert inverted_index.get() == {}
