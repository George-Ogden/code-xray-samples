import pytest

from binary_search import binary_search


def test_binary_search():
    key = "d"
    array = ["a", "b", "c", "d", "e", "f"]
    idx = binary_search(key=key, array=array)
    assert array[idx] == key


def test_binary_search_missing_value():
    key = "d"
    array = ["a", "b", "c", "e", "f"]
    with pytest.raises(ValueError):
        binary_search(key=key, array=array)
