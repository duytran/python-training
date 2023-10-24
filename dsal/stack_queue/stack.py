
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Push the data to stack
        """
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        """
        Returns the data of top element and remove it
        """
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
        
    def peek(self):
        """
        Returns the top of the stack without removing
        """
        if self.top:
            return self.top.data
        else:
            return None