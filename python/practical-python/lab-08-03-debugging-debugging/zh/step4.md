# 使用打印语句进行调试

使用`print()`进行调试非常常见。

提示：确保你使用`repr()`

```python
def spam(x):
    print('DEBUG:', repr(x))
  ...
```

`repr()`会显示值的准确表示形式，而不是美观的打印输出。

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# 不使用 `repr`
>>> print(x)
3.4
# 使用 `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
