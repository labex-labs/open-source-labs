# Global Definitions

Everything defined in the _global_ scope is what populates the module
namespace. Consider two modules
that define the same variable `x`.

```python
# foo.py
x = 42
def grok(a):
    ...
```

```python
# bar.py
x = 37
def spam(a):
    ...
```

In this case, the `x` definitions refer to different variables. One
is `foo.x` and the other is `bar.x`. Different modules can use the
same names and those names won't conflict with each other.

**Modules are isolated.**
