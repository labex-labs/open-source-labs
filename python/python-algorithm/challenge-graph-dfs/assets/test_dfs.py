from dfs import *
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


class TestDfs(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.dfs(nodes[0], self.results.add_result)
        self.assertEqual(str(self.results), "[0, 1, 3, 2, 4, 5]")

        print("Success: test_dfs")


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == "__main__":
    main()
