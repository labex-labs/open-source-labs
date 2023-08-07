# How programs fail

Python performs no checking or validation of function argument types or values. A function will work on any data that is compatible with the statements in the function.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

If there are errors in a function, they appear at run time (as an exception).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

To verify code, there is a strong emphasis on testing (covered later).
