# Example: Receiving messages

In Exercise 8.3, we looked at the definitions of coroutines. Coroutines were functions that you sent data to. For example:

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Got:', item)

>>> p = printer()
>>> p.send('Hello')
Got: Hello
>>> p.send('World')
Got: World
>>>
```

At the time, it might have been interesting to use `yield` to receive a value. However, if you really look at the code, it looks pretty weird--a bare `yield` like that? What's going on there?

In the `cofollow.py` file, define the following function:

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
```

This function receives a message, but then verifies that it is of an expected type. Try it:

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Got:', val)

>>> p = print_ints()
>>> p.send(42)
Got: 42
>>> p.send(13)
Got: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
AssertionError: Expected type <class 'int'>
>>>
```

From a readability point of view, the `yield from receive(int)` statement is a bit more descriptive--it indicates that the function will yield until it receives a message of a given type.

Now, modify all of the coroutines in `coticker.py` to use the new `receive()` function and make sure the code from Exercise 8.3 still works.
