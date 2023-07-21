# Contract Programming

Also known as Design By Contract, liberal use of assertions is an
approach for designing software. It prescribes that software designers
should define precise interface specifications for the components of
the software.

For example, you might put assertions on all inputs of a function.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Checking inputs will immediately catch callers who aren't using
appropriate arguments.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
