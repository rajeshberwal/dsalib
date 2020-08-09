def bubble_sort(array: list) -> None:
    """Sort given list using Bubble Sort technique

    Args:
        array (list): list of elements
    """
    for i in range(len(array)):
        stop = True
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                stop = False
                array[j], array[j - 1] = array[j - 1], array[j]
        if stop:
            break