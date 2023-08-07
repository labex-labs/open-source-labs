# Inline Tests

Assertions can also be used for simple tests.

```python
def add(x, y):
    return x + y

assert add(2,2) == 4
```

This way you are including the test in the same module as your code.

_Benefit: If the code is obviously broken, attempts to import the module will crash._

This is not recommended for exhaustive testing. It's more of a basic "smoke test". Does the function work on any example at all? If not, then something is definitely broken.
