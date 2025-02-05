# continue statement

To skip one element and move to the next one, use the `continue` statement.

```python
for line in lines:
    if line == '\n':    # Skip blank lines
        continue
    # More statements
    ...
```

This is useful when the current item is not of interest or needs to be ignored in the processing.
