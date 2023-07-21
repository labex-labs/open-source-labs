# Modules as Environments

Modules form an enclosing environment for all of the code defined inside.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

_Global_ variables are always bound to the enclosing module (same file).
Each source file is its own little universe.
