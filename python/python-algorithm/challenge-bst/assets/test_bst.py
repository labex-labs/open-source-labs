from solution import *
import unittest
import sys

sys.path.append("/home/labex/project")


def in_order_traversal(node, visit_func):
    if node is not None:
        in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        in_order_traversal(node.right, visit_func)


def pre_order_traversal(node, visit_func):
    if node is not None:
        visit_func(node.data)
        pre_order_traversal(node.left, visit_func)
        pre_order_traversal(node.right, visit_func)


def post_order_traversal(node, visit_func):
    if node is not None:
        post_order_traversal(node.left, visit_func)
        post_order_traversal(node.right, visit_func)
        visit_func(node.data)


class Results(object):
    def __init__(self):
        self.results = []

    def add_result(self, result):
        # TODO: Clean this up
        # Simplifies challenge coding and unit testing
        # but makes this function look less appealing
        self.results.append(int(str(result)))

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)


class TestTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")

        print("Success: test_tree")


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == "__main__":
    main()
