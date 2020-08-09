def linear_search(arr: list, elem: object) -> int or None:
    """Takes list and element that we want to search and use brute force technique on the list. 
    If element is present in the list then it will return the index of that element else it will return None

    Args:
        arr (List): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: if element is present then it will return the index otherwie will return None
    """
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return None