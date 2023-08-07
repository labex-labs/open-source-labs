# Identity and References

Use the `is` operator to check if two values are exactly the same object.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compares the object identity (an integer). The identity can be obtained using `id()`.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Note: It is almost always better to use `==` for checking objects. The behavior of `is` is often unexpected:

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
