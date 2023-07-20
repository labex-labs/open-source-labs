# Enforcement

Modify the `ValidatedFunction` class so that it enforces value checks
attached via function annotations. For example:

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

Hint: To do this, play around with signature binding. Use the `bind()`
method of `Signature` objects to bind function arguments to argument
names. Then cross reference this information with the
`__annotations__` attribute to get the different validator classes.

Keep in mind, you're making an object that looks like a function, but
it's really not. There is magic going on behind the scenes.
