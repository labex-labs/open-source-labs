# Graph Path Exists

## Problem

Given a directed graph and two nodes, write a Python function to determine whether there is a path between the two nodes.

## Requirements

To solve this problem, we need to make the following assumptions:

- The graph is directed.
- We already have Graph and Node classes.
- The graph is connected.
- The inputs are valid.
- The solution fits memory.

## Example Usage

Suppose we have the following graph:

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

We can use the following function to determine whether there is a path between two nodes:

```
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False
```

The first two function calls return True because there is a path between the start and end nodes. The last function call returns False because there is no path between the start and end nodes.
