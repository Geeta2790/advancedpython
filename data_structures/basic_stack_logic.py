class Stack:
    """
    A simple stack implementation using a list.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item of the stack without removing it.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self.items)