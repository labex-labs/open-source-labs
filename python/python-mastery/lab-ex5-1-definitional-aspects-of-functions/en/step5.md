# API Challenge: Type hints

Functions can have optional type-hints attached to arguments and return values. For example:

```python
def add(x:int, y:int) -> int:
    return x + y
```

The `typing` module has additional classes for expressing more complex kinds of types including containers. For example:

```python
from typing import List

def sum_squares(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n*n
    return total
```

Your challenge: Modify the code in `reader.py` so that all functions have type hints. Try to make the type-hints as accurate as possible. To do this, you may need to consult the documentation for the [typing module](https://docs.python.org/3/library/typing.html).
