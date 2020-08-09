class Stack:
    def __init__(self):
        self._top = -1
        self.stack = []
    
    def __len__(self):
        return self._top + 1
    
    def is_empty(self):
        """Returns True is stack is empty otherwise returns False

        Returns:
            bool: True if stack is empty otherwise returns False
        """
        return self._top == -1

    def push(self, data):
        """Add data at the end of the stack.

        Args:
            data (object): element that we want to add
        """
        self.stack.append(data)
        self._top += 1
    
    def pop(self):
        """Remove the last element from stack and returns it's value.

        Raises:
            IndexError: If stack is empty raise an Index error

        Returns:
            object: element that we have removed from stack"""
        if self.is_empty():
            raise IndexError("stack is empty")
        self._top += 1
        return self.stack.pop()
    
    def peek(self):
        """returns the current top element of the stack."""
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.stack[self._top]
    
    def __str__(self):
        return ''.join([str(elem) for elem in self.arr])