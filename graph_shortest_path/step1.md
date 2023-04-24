# Graph Shortest Path

## Problem

Given a directed graph with weighted edges, find the shortest path between two nodes.

## Requirements

To solve this problem, we need to consider the following requirements:

- Is this a directional graph? - Yes
- Could the graph have cycles? - Yes
  - Note: If the answer were no, this would be a DAG.
    - DAGs can be solved with a [topological sort](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)
- Are the edges weighted? - Yes
  - Note: If the edges were not weighted, we could do a BFS
- Are the edges all non-negative numbers? - Yes
  - Note: Graphs with negative edges can be done with Bellman-Ford
    - Graphs with negative cost cycles do not have a defined shortest path
- Do we have to check for non-negative edges? - No
- Can we assume this is a connected graph? - Yes
- Can we assume the inputs are valid? - No
- Can we assume we already have a graph class? - Yes
- Can we assume we already have a priority queue class? - Yes
- Can we assume this fits memory? - Yes

## Example

Consider the following graph:

<pre>
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
</pre>

We can find the shortest path between node 'a' and node 'i' using the ShortestPath class:

<pre>
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
</pre>

The expected result is:

<pre>
['a', 'c', 'd', 'g', 'i']
</pre>

We can also check the weight of the shortest path:

<pre>
self.assertEqual(shortest_path.path_weight['i'], 8)
</pre>
