class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)


class BinaryTree(object):
    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if not self._node_in_tree(root, node1) or not self._node_in_tree(root, node2):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        else:
            return left_node if left_node is not None else right_node


class LcaResult(object):
    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor


class BinaryTreeOptimized(object):
    def lca(self, root, node1, node2):
        if root is None:
            raise TypeError("root cannot be None")
        result = self._lca(root, node1, node2)
        if result.is_ancestor:
            return result.node
        return None

    def _lca(self, curr_node, node1, node2):
        if curr_node is None:
            return LcaResult(None, is_ancestor=False)
        if curr_node is node1 and curr_node is node2:
            return LcaResult(curr_node, is_ancestor=True)
        left_result = self._lca(curr_node.left, node1, node2)
        if left_result.is_ancestor:
            return left_result
        right_result = self._lca(curr_node.right, node1, node2)
        if right_result.is_ancestor:
            return right_result
        if left_result.node is not None and right_result.node is not None:
            return LcaResult(curr_node, is_ancestor=True)
        elif curr_node is node1 or curr_node is node2:
            is_ancestor = left_result.node is not None or right_result.node is not None
            return LcaResult(curr_node, is_ancestor)
        else:
            return LcaResult(
                left_result.node if left_result.node is not None else right_result.node,
                is_ancestor=False,
            )
