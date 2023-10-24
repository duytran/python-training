"""Module providing the code represent list and pointer."""


class Node:
    """
    A class to represent a Node
    """

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class SinglyLinkedList:
    """
    A class to represent a Singly Linked List
    """

    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        """
        Append a node in linked list
        """
        # Encapsulate the data in a Node
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

        # Increase linked list size
        self.size += 1

    def iter(self):
        """
        Iteration a linked list
        """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        """
        Delete a node out of a linked list
        """
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        """
        Search a node in linked list
        """
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        """
        Clear a linked list
        """
        self.tail = None
        self.head = None
