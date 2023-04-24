# Graph Build Order

Problem: Find a build order given a list of projects and dependencies.

## Requirements

- Is it possible to have a cyclic graph as the input?
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

- projects: a, b, c, d, e, f, g
- dependencies: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)
- output: d, f, c, b, g, a, e

Note: Edge direction is down

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

Test a graph with a cycle, output should be None
