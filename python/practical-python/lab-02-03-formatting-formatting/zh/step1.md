# 字符串格式化

在Python 3.6及以上版本中，一种格式化字符串的方法是使用 `f-strings`。

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

`{表达式:格式}` 这部分会被替换。

它通常与 `print` 一起使用。

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
