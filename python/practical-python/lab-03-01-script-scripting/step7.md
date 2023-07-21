# Bottom-up Style

Functions are treated as building blocks.
The smaller/simpler blocks go first.

```python
# myprogram.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Defined above
    ...

def spam(x):
    ...
    bar(x)          # Defined above
    ...

spam(42)            # Code that uses the functions appears at the end
```

Later functions build upon earlier functions. Again, this is only
a point of style. The only thing that matters in the above program
is that the call to `spam(42)` go last.
