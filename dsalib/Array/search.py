def search(arr: list, elem: object) -> int or None:
    """Uses Linear Search for searching the given element.
    It will returns index for given element if element is present in the list.

    Args:
        arr (list): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: if element is present in the list then will return index of that element otherwise return None
    """
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return None