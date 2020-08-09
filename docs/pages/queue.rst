=====
Queue
=====

A Queue is a linear data structure, or more abstractly a sequential collection. The entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.

Usage
-----

::

    from dsalib.Queue import Queue
    # initializing Empty Queue
    queue = Queue()

Queue Operations
----------------

**size():**
    Returns the size of queue

::

    queue.size()

**is_empty()**
    Returns the True if Queue is empty otherwise returns False

::

    queue.is_empty()

**enqueue(data)**
    Add an element at the end of the Queue.

::

    queue.enqueue(5)

**dequeue()**
    Remove last element from Queue and returns it.

::

    queue.dequeue()
