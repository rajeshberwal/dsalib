def insert(arr: list, pos: int, elem: object) -> None:
    """Takes index and element and insert that element at given position in the array

    Args:
        arr (list): list of elements
        pos (int): index on we want to insert given element
        elem (object): element that we want to insert

    Raises:
        Exception: Raise an exception if given index is invalid
    """
    if pos > len(arr):
        raise Exception("Invalid Index")
        return
        
    if pos == len(arr):
        arr.append(elem)
    else:
        arr.append(arr[-1])
        for i in reversed(range(len(arr))):
            arr[i] = arr[i - 1]
        arr[pos] = elem