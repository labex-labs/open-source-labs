# C-Style Formatting

You can also use the formatting operator `%`.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

This requires a single item or a tuple on the right. Format codes are modeled after the C `printf()` as well.

_Note: This is the only formatting available on byte strings._

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # %b may be used instead of %s
b'Dave has 37 messages'
>>>
```
