# Step 1 Solution

Write the following program to `muint.py`:

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Then, run this program in your terminal with the following command:

```bash
python3 -i mutint.py
```

Run the following code in the `Python Shell`:

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```