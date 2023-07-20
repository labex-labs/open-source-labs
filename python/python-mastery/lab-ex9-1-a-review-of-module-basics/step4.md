# from module import

Restart Python and import a selected symbol from a module.

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
>>>
```

Notice how this loaded the entire module (observe the output of
the print function and how the `x` variable is used).

When you use `from`, the module object itself is not
visible. For example:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
>>>
```

Make sure you understand that when you export things from a module,
they are simply name references. For example, try this and explain:

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x is 42
>>> x = 13
>>> foo()
x is 42                   # !! Please explain
>>> x
13
>>>
```
