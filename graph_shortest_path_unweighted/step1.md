# Graph Shortest Path Unweighted

## Problem

Given a directed graph with no edge weights, find the shortest path between two nodes.

## Requirements

To solve this problem, the following requirements must be met:

- The graph is directed.
- The graph is unweighted.
- Graph and Node classes are already available.
- The inputs are two nodes.
- The output is a list of node keys that make up the shortest path.
- If there is no path, return None.
- The graph is connected.
- The inputs are valid.
- The algorithm must fit memory.

## Example Usage

Suppose we have the following graph:

```
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
```

We can find the shortest path between two nodes using the `search_path` function:

- `search_path(start=0, end=2) -> [0, 1, 3, 2]`
- `search_path(start=0, end=0) -> [0]`
- `search_path(start=4, end=5) -> None`
