# Preparation

We're going to recreate the `Stock` class from scratch using some new techniques. Make sure you have your unit tests from [Exercise 5.4](ex5_4.md) handy. You'll want those.

If you define a function, you probably already know that it can be called using a mix of positional or keyword arguments. For example:

```python
>>> def foo(x, y, z):
        return x + y + z

>>> foo(1, 2, 3)
6
>>> foo(1, z=3, y=2)
6
>>>
```

You may also know that you can pass sequences and dictionaries as function arguments using the \* and \*\* syntax. For example:

```python
>>> args = (1, 2, 3)
>>> foo(*args)
6
>>> kwargs = {'y':2, 'z':3 }
>>> foo(1,**kwargs)
6
>>>
```

In addition to that, you can write functions that accept any number of positional or keyword arguments using the \* and \*\* syntax. For example:

```python
>>> def foo(*args):
        print(args)

>>> foo(1,2)
(1, 2)
>>> foo(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> foo()
()
>>>
>>> def bar(**kwargs):
        print(kwargs)

>>> bar(x=1,y=2)
{'y': 2, 'x': 1}
>>> bar(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> bar()
{}
>>>
```

Variable argument functions are sometimes useful as a technique for reducing or simplifying the amount of code you need to type. In this exercise, we'll explore that idea for simple data structures.
