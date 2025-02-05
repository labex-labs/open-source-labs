# 字典的键

编写一个函数 `keys_only(flat_dict)`，该函数以扁平字典作为输入，并返回其所有键的列表。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `dict.keys()` 返回给定字典中的键。
2. 返回前一步结果的 `list()`。

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
