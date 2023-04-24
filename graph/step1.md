# Graph

## Problem

Implement a graph that satisfies the following requirements:

### Requirements

- The graph can be directed or undirected.
- The edges can have weights.
- The graph can have cycles.
- If we try to add a node that already exists, we just do nothing.
- If we try to delete a node that doesn't exist, we just do nothing.
- We can assume this is a connected graph.
- We can assume the inputs are valid.
- We can assume this fits memory.

## Example Usage

Input:

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 6)
graph.add_edge(4, 0, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 9)
```

Result:

- The nodes `0`, `1`, `2`, `3`, `4`, and `5` are connected with specified weights.

Note:

- The Graph class will be used as a building block for more complex graph challenges.
