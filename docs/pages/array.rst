=====
Array
=====

Arrays (data structure) are a type of linear data structure that can hold an ordered collection of values. As opposed to the array (ADT), the array data structure specifies an implementation that the values are of homogeneous size and stored in contiguous memory.

Importing::

    from dsalib import Array

Insertion
=========

**insert(arr, pos, elem):**

    Takes index and element and insert that element at given position in the array

    Args:
        arr (list): list of elements
        pos (int): index on we want to insert given element
        elem (object): element that we want to insert

    Raises:
        Exception: Raise an exception if given index is invalid

    **Usage**::

        arr = [21, 2, 3, 31, 45]
        Array.insert(arr, 3, 62)

Deletion
========

**remove(arr, elem):**
    Takes list and element as argumnents and remove the first element that you have provided

    Args:
        arr (list): list of elements
        elem (object): element that we want to remove

    **Usage**::

        arr = [21, 2, 3, 31, 45]
        Array.remove(arr, 3)

Searching
=========

**search(arr, elem):**
    Uses Linear Search for searching the given element.
    It will returns index for given element if element is present in the list.

    Args:
        arr (list): list of elements
        elem (object): element that we want to search

    Returns:
        int or None: if element is present in the list then will return index of that element otherwise return None
    
    **Usage**::

        arr = [21, 2, 3, 31, 45]
        Array.search(arr, 45)

Sorting
=======

**sort(array):**
    Takes a list and perform mergeSort operation on it.

    Args:
        array (list): list of elements

    **Usage**::

        arr = [21, 2, 3, 31, 45]
        Array.sort(arr, 45)