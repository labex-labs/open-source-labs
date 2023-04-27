# Graph Path Exists

Problem: Determine whether there is a path between two nodes in a graph.

## Requirements

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

## Example Usage

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
