# Catching and Handling Exceptions

Exceptions can be caught and handled.

To catch, use the `try - except` statement.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
    ...
```

The name `ValueError` must match the kind of error you are trying to catch.

It is often difficult to know exactly what kinds of errors might occur in advance depending on the operation being performed. For better or for worse, exception handling often gets added _after_ a program has unexpectedly crashed (i.e., "oh, we forgot to catch that error. We should handle that!").
