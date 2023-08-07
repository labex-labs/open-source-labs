# Modules and import

Any Python source file is a module.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

The `import` statement loads and _executes_ a module.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
