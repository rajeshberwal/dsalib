def insertion_sort(array: list) -> None:
    """Sort given list using Merge Sort Technique.
    Time Complexity: 
        Best Case: O(n),
        Average Case: O(n ^ 2)
        Worst Case: O(n ^ 2)

    Args:
        array (list): list of elements
    """
    for i in range(1, len(array)):
        current_num = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > current_num:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                array[j + 1] = current_num
                break