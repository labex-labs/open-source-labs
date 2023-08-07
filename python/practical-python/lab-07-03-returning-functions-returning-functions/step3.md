# Closures

When an inner function is returned as a result, that inner function is known as a _closure_.

```python
def add(x, y):
    # `do_add` is a closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_Essential feature: A closure retains the values of all variables needed for the function to run properly later on._ Think of a closure as a function plus an extra environment that holds the values of variables that it depends on.
