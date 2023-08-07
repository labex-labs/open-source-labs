# Raising Exceptions

In the file `cofollow.py`, you created a coroutine `printer()`. Modify the code to catch and report exceptions like this:

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Now, try an experiment:

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERROR: ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

Notice how the running generator is not terminated by the exception. This is merely allowing the `yield` statement to signal an error instead of receiving a value.
