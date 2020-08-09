def selection_sort(array: list) -> None:
    """Sort given list using Selection Sort Technique

    Args:
        array (list): list of elements
    """
    for i in range(len(array) - 1):
        minimum: int = i

        # Compare i and i + 1 element
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]