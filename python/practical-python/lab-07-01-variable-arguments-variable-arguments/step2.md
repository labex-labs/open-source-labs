# Keyword variable arguments (\*\*kwargs)

A function can also accept any number of keyword arguments.
For example:

```python
def f(x, y, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The extra keywords are passed in a dictionary.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
```
