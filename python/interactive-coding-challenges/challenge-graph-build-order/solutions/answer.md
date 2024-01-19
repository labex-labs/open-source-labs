# Solution Notebook

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Find a build order given a list of projects and dependencies.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is it possible to have a cyclic graph as the input?
  - Yes
- Can we assume we already have Graph and Node classes?
  - Yes
- Can we assume this is a connected graph?
  - Yes
- Can we assume the inputs are valid?
  - Yes
- Can we assume this fits memory?
  - Yes

## Test Cases

- projects: a, b, c, d, e, f, g
- dependencies: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)
- output: d, f, c, b, g, a, e

Note: Edge direction is down

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

Test a graph with a cycle, output should be None

## Algorithm

We can determine the build order using a topological sort.

- Build the graph with projects (nodes) and dependencies (directed edges)
- Add initially non-dependent nodes to processed_nodes
  - If none exist, we have a circular dependency, return None
- While the length processed_nodes < the length of graph nodes
  - Remove outgoing edges from newly added items in processed_nodes
  - Add non-dependent nodes to processed_nodes
    - If we didn't add any nodes, we have a circular dependency, return None
- Return processed_nodes

Complexity:

- Time: O(V + E)
- Space: O(V + E)

## Code

```python
from collections import deque


class Dependency(object):

    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after
```

```python
%run ../graph/graph.py
```

```python
class BuildOrder(object):

    def __init__(self, dependencies):
        self.dependencies = dependencies
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for dependency in self.dependencies:
            self.graph.add_edge(dependency.node_key_before,
                                dependency.node_key_after)

    def _find_start_nodes(self, processed_nodes):
        nodes_to_process = {}
        for key, node in self.graph.nodes.items():
            if node.incoming_edges == 0 and key not in processed_nodes:
                nodes_to_process[key] = node
        return nodes_to_process

    def _process_nodes(self, nodes_to_process, processed_nodes):
        for node in nodes_to_process.values():
            # We'll need to iterate on copies since we'll need
            # to change the dictionaries during iteration with
            # the remove_neighbor call
            for adj_node in list(node.adj_nodes.values()):
                node.remove_neighbor(adj_node)
            processed_nodes[node.key] = node
        nodes_to_process = {}

    def find_build_order(self):
        result = []
        nodes_to_process = {}
        processed_nodes = {}
        while len(result) != len(self.graph.nodes):
            nodes_to_process = self._find_start_nodes(processed_nodes)
            if not nodes_to_process:
                return None
            result.extend(nodes_to_process.values())
            self._process_nodes(nodes_to_process, processed_nodes)
        return result
```

## Unit Test

```python
%run ../utils/results.py
```

```python
%%writefile test_build_order.py
import unittest


class TestBuildOrder(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBuildOrder, self).__init__()
        self.dependencies = [
            Dependency('d', 'g'),
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')
        expected_result1 = ('c', 'b', 'g')
        self.assertTrue(processed_nodes[0].key in expected_result0)
        self.assertTrue(processed_nodes[1].key in expected_result0)
        self.assertTrue(processed_nodes[2].key in expected_result1)
        self.assertTrue(processed_nodes[3].key in expected_result1)
        self.assertTrue(processed_nodes[4].key in expected_result1)
        self.assertTrue(processed_nodes[5].key is 'a')
        self.assertTrue(processed_nodes[6].key is 'e')

        print('Success: test_build_order')

    def test_build_order_circular(self):
        self.dependencies.append(Dependency('e', 'f'))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        self.assertTrue(processed_nodes is None)

        print('Success: test_build_order_circular')


def main():
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


if __name__ == '__main__':
    main()
```

    Overwriting test_build_order.py

```python
%run -i test_build_order.py
```

    Success: test_build_order
    Success: test_build_order_circular
