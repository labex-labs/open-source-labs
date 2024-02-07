# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Implement depth-first search on a graph.

- [Constraints](#Constraints)
- [Test Cases](#Test-Cases)
- [Algorithm](#Algorithm)
- [Code](#Code)
- [Unit Test](#Unit-Test)

## Constraints

- Is the graph directed?
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

Input:

- `add_edge(source, destination, weight)`

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
```

Result:

- Order of nodes visited: [0, 1, 3, 2, 4, 5]

## Algorithm

If we want to visit every node in a graph, we generally prefer depth-first search since it is simpler (no need to use a queue). For shortest path, we generally use breadth-first search.

- Visit the current node and mark it visited
- Iterate through each adjacent node
  - If the node has not been visited, call dfs on it

Complexity:

- Time: O(V + E), where V = number of vertices and E = number of edges
- Space: O(V), for the recursion depth

## Code

```python
%run ../graph/graph.py
```

```python
class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visit_state = State.visited
        for node in root.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.dfs(node, visit_func)
```

## Unit Test

```python
%run ../utils/results.py
```

```python
%%writefile test_dfs.py
import unittest


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

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
```

    Overwriting test_dfs.py

```python
%run -i test_dfs.py
```

    Success: test_dfs
