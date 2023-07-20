# The Three Operations

The entire Python object system consists of just three core operations: getting, setting, and deleting
of attributes. Normally, these are accessed via the dot (.) like this:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    #  get
'GOOG'
>>> s.shares = 50    # set
>>> del s.shares     # delete
>>>
```

The three operations are also available as functions. For example:

```python
>>> getattr(s, 'name')            # Same as s.name
'GOOG'
>>> setattr(s, 'shares', 50)      # Same as s.shares = 50
>>> delattr(s, 'shares')          # Same as del s.shares
>>>
```

An additional function `hasattr()` can be used to probe an object for the existence of an attribute:

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
