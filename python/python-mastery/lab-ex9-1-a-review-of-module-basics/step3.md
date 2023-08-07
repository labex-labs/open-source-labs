# Repeated Module Loading

Make sure you understand that modules are only loaded
once. Try a repeated import and notice how you do not see
the output from the `print` function:

```python
>>> import simplemod
>>>
```

Try changing the value of `x` and see that a repeated import
has no effect.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

Use `importlib.reload()` if you want to force a module to reload.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` is a dictionary of all loaded modules. Take
a look at it, delete your module, and try a repeated import.

```python
>>> sys.modules
... look at output ...
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>>
```
