# 可选参数优先使用关键字参数

比较并对比以下两种不同的调用方式：

```python
parse_data(data, False, True) #?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

在大多数情况下，关键字参数能提高代码的清晰度，尤其是对于用作标志或与可选功能相关的参数。
