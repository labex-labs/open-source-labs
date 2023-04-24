# Graph Build Order

## Problem

Given a list of projects and their dependencies, we need to find a valid build order. A build order is a list of projects in which each project appears before any project that depends on it.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input may contain a cyclic graph.
- We can assume that we already have Graph and Node classes.
- We can assume that the graph is connected.
- We can assume that the inputs are valid.
- We can assume that the problem fits memory.

## Example

Suppose we have the following projects and dependencies:

- projects: a, b, c, d, e, f, g
- dependencies: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)

The output should be: d, f, c, b, g, a, e

Note that the edge direction is down, meaning that a project depends on the projects below it.

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

If the input contains a cyclic graph, the output should be None.
