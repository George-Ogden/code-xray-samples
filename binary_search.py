# Modified from https://stackoverflow.com/a/212413/12103577.
def binary_search(key, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        value = array[mid]
        if value < key:
            low = mid + 1
        elif value > key:
            high = mid - 1
        else:
            return mid
    raise ValueError(f"{key!r} not found")
