# Solutions

This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

## Problem: Determine whether there is a path between two nodes in a graph.

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

- search_path(start=0, end=2) -> True
- search_path(start=0, end=0) -> True
- search_path(start=4, end=5) -> False

## Algorithm

To determine if there is a path, we can use either breadth-first or depth-first search.

Breadth-first search can also be used to determine the shortest path. Depth-first search is easier to implement with just straight recursion, but often results in a longer path.

We'll use a breadth-first search approach:

- Add the start node to the queue and mark it as visited
- If the start node is the end node, return True
- While the queue is not empty
  - Dequeue a node and visit it
  - If the node is the end node, return True
  - Iterate through each adjacent node
    - If the node has not been visited, add it to the queue and mark it as visited
- Return False

Complexity:

- Time: O(V + E), where V = number of vertices and E = number of edges
- Space: O(V + E)

## Code

```python
%run ../graph/graph.py
```

```python
from collections import deque


class GraphPathExists(Graph):

    def path_exists(self, start, end):
        if start is None or end is None:
            return False
        if start is end:
            return True
        queue = deque()
        queue.append(start)
        start.visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node is end:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False
```

## Unit Test

```python
%%writefile test_path_exists.py
import unittest


class TestPathExists(unittest.TestCase):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
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

        self.assertEqual(graph.path_exists(nodes[0], nodes[2]), True)
        self.assertEqual(graph.path_exists(nodes[0], nodes[0]), True)
        self.assertEqual(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()
```

    Overwriting test_path_exists.py

```python
%run -i test_path_exists.py
```

    Success: test_path_exists
