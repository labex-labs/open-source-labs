# Understanding Module Loading Behavior

Python has some interesting behaviors regarding module loading. Let us explore them in this step.

1. In the same Python interpreter session, try importing the module again:

```python
>>> import simplemod
```

Notice that this time you do not see the "Loaded simplemod" output. This is because **Python only loads a module once** per interpreter session. Subsequent `import` statements do not reload the module.

2. You can modify the variables in a module after importing it:

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

3. Importing the module again does not reset the changes:

```python
>>> import simplemod
>>> simplemod.x
13
```

4. To forcibly reload a module, you need to use the `importlib.reload()` function:

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

The module has been reloaded, and the value of `x` has been reset to `42`.

5. Python keeps track of all loaded modules in the `sys.modules` dictionary:

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

6. You can remove a module from this dictionary to force Python to reload it on the next import:

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

The module was loaded again because it was removed from `sys.modules`.
