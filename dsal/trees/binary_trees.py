from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right_child = None
        self.left_child = None


class BinaryTree:
    def __init__(self) -> None:
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # Get children count
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif node.left_child is None and node.right_child is None:
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.left_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def inorder_traversal(self, root_node):
        # In-order traversal and infix notation
        current = root_node
        if current is None:
            return
        self.inorder_traversal(current.left_child)
        print(current.data)
        self.inorder_traversal(current.right_child)

    def preorder_traversal(self, root_node):
        # Pre-order traversal and prefix notation
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder_traversal(current.left_child)
        self.preorder_traversal(current.right_child)

    def postorder_traversal(self, root_node):
        # Post-order traversal and postfix notation.
        current = root_node
        if current is None:
            return
        self.postorder_traversal(current.left_child)
        self.postorder_traversal(current.right_child)

        print(current.data)

    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left_child)

            if node.right_child:
                traversal_queue.append(node.right_child)

        return list_of_nodes
