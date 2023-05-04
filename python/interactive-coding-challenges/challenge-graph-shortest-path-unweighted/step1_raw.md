# Graph Shortest Path Unweighted

Problem: Find the shortest path between two nodes in a graph.

## Requirements

- Is the graph directed?
  - Yes
- Is the graph weighted?
  - No
- Can we assume we already have Graph and Node classes?
  - Yes
- Are the inputs two Nodes?
  - Yes
- Is the output a list of Node keys that make up the shortest path?
  - Yes
- If there is no path, should we return None?
  - Yes
- Can we assume this is a connected graph?
  - Yes
- Can we assume the inputs are valid?
  - Yes
- Can we assume this fits memory?
  - Yes

## Example Usage

Input:

- `add_edge(source, destination, weight)`

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

Result:

- search_path(start=0, end=2) -> [0, 1, 3, 2]
- search_path(start=0, end=0) -> [0]
- search_path(start=4, end=5) -> None
