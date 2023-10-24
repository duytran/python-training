"""Module providing the code represent double linked list"""


class Node(object):
    """
    The node data in linked list
    """
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = None
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    """
    Double linked list
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """
        Append an item to the list.
        """

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def delete(self, data):
        """
        Delete an item out of list
        """
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True

                current = current.next

        if node_deleted:
            self.count -= 1

    def iter(self):
        """
        Iteration a linked list
        """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        """
        Check the node data exist in the list
        """
        for node_data in self.iter():
            if data == node_data:
                return True
        return False
