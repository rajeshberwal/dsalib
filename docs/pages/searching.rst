=================
Search Algorithms
=================

The searching algorithms are used to search or find one or more than one element from a dataset. These type of algorithms are used to find elements from a specific data structures. Searching may be sequential or not. If the data in the dataset are random, then we need to use sequential searching.

**Importing Search Algorithms**::

    from dsalib import Search

Linear Search
-------------

**linear_search(arr, elem):**
    Takes list and element that we want to search and use brute force technique on the list. 
    If element is present in the list then it will return the index of that element else it will return None

    Args:
        arr (List): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: if element is present then it will return the index otherwie will return None

    Usage::

        arr = [33, 12, 43, 51]
        Search.linear_search(arr, 12)

Binary Search
-------------

**binary_search(array, elem)**
    Binary Search is only used on sorted Array.
    If element is present in the list then it will return the index of that element else it will return None

    Args:
        array (list): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: will return int if elem is present in the list else will return None

    Usage::

        arr = [2, 13, 45, 63, 123]
        Search.binary_search(arr, 45)
 