import unittest
import sys

sys.path.append("/home/labex/project")
from answer import *


class TestBuildOrder(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBuildOrder, self).__init__()
        self.dependencies = [
            Dependency("d", "g"),
            Dependency("f", "c"),
            Dependency("f", "b"),
            Dependency("f", "a"),
            Dependency("c", "a"),
            Dependency("b", "a"),
            Dependency("a", "e"),
            Dependency("b", "e"),
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()

        expected_result0 = ("d", "f")
        expected_result1 = ("c", "b", "g")
        self.assertTrue(processed_nodes[0].key in expected_result0)
        self.assertTrue(processed_nodes[1].key in expected_result0)
        self.assertTrue(processed_nodes[2].key in expected_result1)
        self.assertTrue(processed_nodes[3].key in expected_result1)
        self.assertTrue(processed_nodes[4].key in expected_result1)
        self.assertTrue(processed_nodes[5].key == "a")
        self.assertTrue(processed_nodes[6].key == "e")

        print("Success: test_build_order")

    def test_build_order_circular(self):
        self.dependencies.append(Dependency("e", "f"))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        self.assertTrue(processed_nodes is None)

        print("Success: test_build_order_circular")


def main():
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


if __name__ == "__main__":
    main()
