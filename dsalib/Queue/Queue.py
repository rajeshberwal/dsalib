class Queue:
    """Queue Data Structure
    Implementation of Queue Data Structure
    """
    def __init__(self):
        self.queue = []
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        return ' '.join([str(elem) for elem in self.queue])

    def size(self) -> int:
        """Returns the size of queue

        Returns:
            int: size of queue
        """
        return self.size

    def is_empty(self) -> bool:
        """Returns the True if Queue is empty otherwise returns False

        Returns:
            bool: description
        """
        return self.size <= 0

    def enqueue(self, data: object) -> None:
        """Add an element at the end of the Queue.

        Args:
            data (object): element that we want to insert in the queue

        Returns:
            None: [Returns Nothing
        """
        self.queue.append(data)

        # assign the rear as size of the queue and front as 0
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def dequeue(self) -> object:
        """Remove last element from Queue and returns it.

        Returns:
            object: last element of Queue
        """
        if self.is_empty():
            # queue underflow
            return -1
        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
            return self.queue.pop(0)