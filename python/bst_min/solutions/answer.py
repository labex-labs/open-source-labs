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
            raise TypeError("data cannot be None")
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


class MinBst(object):
    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array) - 1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid - 1)
        node.right = self._create_min_bst(array, mid + 1, end)
        return node
