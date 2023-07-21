# Example: Keeping a History

Problem: We want a history of the last N things.
Solution: Use a `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
        ...
```

The `collections` module might be one of the most useful library
modules for dealing with special purpose kinds of data handling
problems such as tabulating and indexing.

In this exercise, we’ll look at a few simple examples. Start by
running your `report.py` program so that you have the portfolio of
stocks loaded in the interactive mode.

```bash
$ python3 -i report.py
```
