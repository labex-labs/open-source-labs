# Module Loading and System Path

Try importing the module you just created:

```python
>>> import simplemod
Loaded simplemod
>>> simplemod.foo()
x is 42
>>>
```

If this failed with an `ImportError`, your path setting is flaky. Look at the value of `sys.path` and fix it.

```python
>>> import sys
>>> sys.path
... look at the result ...
>>>
```
