# Everything is an object

Numbers, strings, lists, functions, exceptions, classes, instances,
etc. are all objects. It means that all objects that can be named can
be passed around as data, placed in containers, etc., without any
restrictions. There are no _special_ kinds of objects. Sometimes it
is said that all objects are "first-class".

A simple example:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

Here, `items` is a list containing a function, a module and an
exception. You can directly use the items in the list in place of the
original names:

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

With great power comes responsibility. Just because you can do that doesn't mean you should.

In this set of exercises, we look at some of the power that comes from first-class
objects.
