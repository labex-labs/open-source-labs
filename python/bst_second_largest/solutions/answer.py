class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

class Solution(Bst):

    def _find_second_largest(self, node):
        if node.right is not None:
            if node.right.left is not None or node.right.right is not None:
                return self._find_second_largest(node.right)
            else:
                return node
        else:
            return self._find_right_most_node(node.left)

    def _find_right_most_node(self, node):
        if node.right is not None:
            return self._find_right_most_node(node.right)
        else:
            return node

    def find_second_largest(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        if self.root.right is None and self.root.left is None:
            raise ValueError('root must have at least one child')
        return self._find_second_largest(self.root)
