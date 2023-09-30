# Shallow copies

Lists and dicts have methods for copying.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Make a copy
>>> a is b
False
```

It's a new list, but the list items are shared.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

For example, the inner list `[100, 101, 102]` is being shared. This is known as a shallow copy. Here is a picture.

![Shallow copy](./assets/shallow.png)
