# Closures as a data structure

One potential use of closures is as a tool for data encapsulation. Try this
example:

```python
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

This code defines two inner functions that manipulate a value. Try it out:

```python
>>> up, down = counter(0)
>>> up()
1
>>> up()
2
>>> up()
3
>>> down()
2
>>> down()
1
>>>
```

Notice how there is no class definition involved here. Moreover,
there is no global variable either. Yet, the `up()` and `down()`
functions are manipulating some "behind the scenes" value. It's
fairly magical.
