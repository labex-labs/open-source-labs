from tree_level_lists import *
import unittest
import sys

sys.path.append("/home/labex/project")


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


class TestTreeLevelLists(unittest.TestCase):
    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        levels = bst.create_level_lists()
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        self.assertEqual(str(results_list[0]), "[5]")
        self.assertEqual(str(results_list[1]), "[3, 8]")
        self.assertEqual(str(results_list[2]), "[2, 4, 7, 9]")
        self.assertEqual(str(results_list[3]), "[1, 6, 10]")
        self.assertEqual(str(results_list[4]), "[11]")

        print("Success: test_tree_level_lists")


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == "__main__":
    main()
