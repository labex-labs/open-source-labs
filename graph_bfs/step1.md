# Graph Bfs

## Problem

Implementing BFS on a graph involves visiting all the vertices of the graph in breadth-first order, starting from a given source vertex. The algorithm works by visiting the source vertex, then visiting all its neighbors, then visiting all the neighbors of its neighbors, and so on. The order in which the vertices are visited is important, as it determines the shortest path from the source vertex to all other vertices in the graph.

## Requirements

To implement BFS on a graph, the following requirements must be met:

- The graph is directed.
- Graph and Node classes are already available.
- The graph is connected.
- The inputs are valid.
- The algorithm fits memory.

## Example Usage

Suppose we have a graph with the following edges:

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

If we start BFS from vertex 0, the order of nodes visited will be [0, 1, 4, 5, 3, 2]. This means that vertex 0 is visited first, followed by its neighbors 1, 4, and 5, then the neighbors of 1 (3 and 4), then the neighbor of 3 (2).
