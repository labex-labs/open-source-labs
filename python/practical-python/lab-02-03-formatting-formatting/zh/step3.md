# 字典格式化

你可以使用 `format_map()` 方法对值的字典应用字符串格式化：

```python
>>> s = {
    'name': 'IBM',
   'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

它使用与 `f-strings` 相同的代码，但从提供的字典中获取值。
