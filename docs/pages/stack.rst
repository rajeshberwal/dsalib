=====
Stack
=====

A stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.

Usage
-----

::

    from dsalib.Stack import Stack
    # initializing Empty Stack
    stack = Stack()

Stack Operations
----------------

**is_empty()**
    Returns True is stack is empty otherwise returns False

::

    stack.is_empty()

**push(data)**
    Add data at the end of the stack.

::

    stack.push(5)

**pop()**
    Remove the last element from stack and returns it's value.

::

    stack.pop()

**peek()**
    returns the current top element of the stack.

::

    stack.peek()