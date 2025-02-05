# 字典查找

你可以测试键是否存在。

```python
if key in d:
    # 存在
else:
    # 不存在
```

你可以查找一个可能不存在的值，并在其不存在时提供一个默认值。

```python
name = d.get(key, default)
```

一个示例：

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
