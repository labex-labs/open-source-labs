# 出力の修正

オブジェクトに `__str__()`、`__repr__()`、`__format__()` などのメソッドを与えることで出力を修正できます。たとえば：

```python
# mint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)
```

試してみましょう。

```python
>>> a = MutInt(3)
>>> print(a)
3
>>> a
MutInt(3)
>>> f'The value is {a:*^10d}'
The value is ****3*****
>>> a.value = 42
>>> a
MutInt(42)
>>>
```
