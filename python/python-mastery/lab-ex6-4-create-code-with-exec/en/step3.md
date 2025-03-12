# Examining How Python's Standard Library Uses exec()

Python's standard library uses the `exec()` function in various places to dynamically generate code. One of the most prominent examples is the `namedtuple` function from the `collections` module.

Let's explore how `namedtuple` works and how it uses `exec()` behind the scenes. Open your Python shell:

```bash
python3
```

First, let's see how `namedtuple` is used:

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name', 'shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]  # namedtuples also support indexing
100
```

A `namedtuple` is a tuple-like object that has fields accessible by attribute lookup as well as being indexable and iterable. It's a convenient way to define simple classes for storing data.

Now, let's look at how `namedtuple` is implemented. We can use the `inspect` module to view its source code:

```python
>>> import inspect
>>> from collections import namedtuple
>>> print(inspect.getsource(namedtuple))
```

You'll see a significant amount of code, but if you look carefully, you'll find that `namedtuple` uses `exec()` to dynamically create a class. The function constructs a string containing Python code for a class definition and then executes it using `exec()`.

This approach allows `namedtuple` to create classes with custom field names at runtime based on the arguments provided. It's a practical example of how `exec()` can be used to generate code dynamically in a real-world application.

Some key points to note about `namedtuple`'s implementation:

1. It uses string formatting to construct a class definition
2. It handles validation of field names
3. It provides additional features like docstrings and methods
4. It executes the generated code using `exec()`

This pattern is similar to what we implemented in our `create_init()` method, but on a more sophisticated level.
