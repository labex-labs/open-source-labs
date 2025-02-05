# Positional variable arguments (\*args)

A function that accepts _any number_ of arguments is said to use variable arguments. For example:

```python
def f(x, *args):
    ...
```

Function call.

```python
f(1,2,3,4,5)
```

The extra arguments get passed as a tuple.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
