# Logging Example

Consider a function.

```python
def add(x, y):
    return x + y
```

Now, consider the function with some logging added to it.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

Now a second function also with some logging.

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
