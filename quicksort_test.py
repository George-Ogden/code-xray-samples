from quicksort import quicksort


def test_quicksort():
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    assert sorted(arr.copy()) == quicksort(arr)
