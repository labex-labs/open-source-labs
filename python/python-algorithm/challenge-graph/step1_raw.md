# Graph

Problem: Implement a graph.

## Requirements

- Is the graph directed?
  - Implement both
- Do the edges have weights?
  - Yes
- Can the graph have cycles?
  - Yes
- If we try to add a node that already exists, do we just do nothing?
  - Yes
- If we try to delete a node that doesn't exist, do we just do nothing?
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

- `source` and `destination` nodes within `graph` are connected with specified `weight`.

Note:

- The Graph class will be used as a building block for more complex graph challenges.
