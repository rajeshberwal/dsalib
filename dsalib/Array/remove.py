from .. import search

def remove(arr: list, elem: object) -> None:
    """Takes list and element as argumnents and remove the first element that you have provided

    Args:
        arr (list): list of elements
        elem (object): element that we want to remove
    """
    idx = search.linear_search(arr, elem)
    
    for i in range(idx, len(arr) - 1):
        arr[i] = arr[i + 1]
    del arr[-1]