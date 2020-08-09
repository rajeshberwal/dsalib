def binary_search(array: list, elem: object) -> int or None:
    """Binary Search is only used on sorted Array.
    If element is present in the list then it will return the index of that element else it will return None

    Args:
        array (list): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: will return int if elem is present in the list else will return None
    """
    low, high = 0, len(array) - 1
    while lo <= hi:
        mid = low + ((high - low) // 2)
        val = array[mid]
        if val == elem:
            return mid
        elif val < elem:
            low = mid + 1
        else:
            high = mid - 1
    return None