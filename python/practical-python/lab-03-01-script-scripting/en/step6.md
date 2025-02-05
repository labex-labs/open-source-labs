# Function Definition

Functions can be _defined_ in any order.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# OR
def bar(x):
    statements

def foo(x):
    bar(x)
```

Functions must only be defined prior to actually being _used_ (or called) during program execution.

```python
foo(3)        # foo must be defined already
```

Stylistically, it is probably more common to see functions defined in a _bottom-up_ fashion.
