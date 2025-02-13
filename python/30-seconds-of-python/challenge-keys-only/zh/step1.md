# 字典的键

## 问题

编写一个函数 `keys_only(flat_dict)`，该函数以扁平字典作为输入，并返回其所有键的列表。

要解决此问题，你可以按以下步骤操作：

1. 使用 `dict.keys()` 返回给定字典中的键。
2. 返回前一个结果的 `list()`。

## 示例

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
