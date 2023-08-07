# Inspecting functions

Define a simple function:

```python
>>> def add(x,y):
       'Adds two things'
       return x+y

>>>
```

Do a `dir()` on the function to look at its attributes.

```python
>>> dir(add)
... look at the result ...
>>>
```

Get some basic information such as the function name, defining module name, and documentation string.

```python
>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>> add.__doc__
'Adds two things'
>>>
```

The `__code__` attribute of a function has low-level information about
the function implementation. See if you can look at this and
determine the number of required arguments and names of local
variables.
