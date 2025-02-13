# 合并字典值

## 问题

编写一个函数 `combine_values(*dicts)`，该函数接受两个或更多字典作为参数，并返回一个新字典，该字典合并了输入字典的值。该函数应执行以下步骤：

1. 创建一个新的 `collections.defaultdict`，每个键的默认值为 `list`。
2. 遍历输入字典，对于每个字典：
   - 遍历字典的键。
   - 将键的值追加到 `defaultdict` 中该键的值列表中。
3. 使用 `dict()` 函数将 `defaultdict` 转换为常规字典。
4. 返回结果字典。

该函数应具有以下签名：

```python
def combine_values(*dicts):
    pass
```

## 示例

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
