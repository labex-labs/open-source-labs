# Graph Dfs

## Problem

Implement depth-first search on a directed graph. The algorithm should start at a given node and visit all reachable nodes in the graph. The order in which the nodes are visited should be recorded and returned as a list.

## Requirements

To implement DFS on a directed graph, the following requirements must be met:

- The graph is directed.
- Graph and Node classes are already implemented.
- The graph is connected.
- The inputs are valid.
- The algorithm fits memory.

## Example Usage

Suppose we have a directed graph with the following edges:

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

If we start DFS at node 0, the order of nodes visited should be [0, 1, 3, 2, 4, 5].
