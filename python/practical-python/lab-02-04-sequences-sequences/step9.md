# enumerate() function

The `enumerate` function adds an extra counter value to iteration.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

The general form is `enumerate(sequence [, start = 0])`. `start` is optional.
A good example of using `enumerate()` is tracking line numbers while reading a file:

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

In the end, `enumerate` is just a nice shortcut for:

```python
i = 0
for x in s:
    statements
    i += 1
```

Using `enumerate` is less typing and runs slightly faster.
