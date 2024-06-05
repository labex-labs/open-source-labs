# Preparation

Back in Exercise 4.3, you created a series of `Validator` classes for performing different kinds of type and value checks. For example:

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

You could use the validators in functions like this:

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

In this exercise, we're going to take it just one step further.
