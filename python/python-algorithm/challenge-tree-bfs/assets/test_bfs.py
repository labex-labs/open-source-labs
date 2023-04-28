from bfs import *
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


class TestBfs(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), "[5, 2, 8, 1, 3]")

        print("Success: test_bfs")


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == "__main__":
    main()
