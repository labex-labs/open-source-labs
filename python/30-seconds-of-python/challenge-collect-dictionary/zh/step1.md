# 反转字典

## 问题

编写一个函数 `invert_dictionary(obj)`，该函数接受一个字典 `obj` 作为输入，并返回一个键值反转后的新字典。输入字典将具有非唯一的可哈希值。如果两个或多个键具有相同的值，函数应将这些键追加到输出字典中的一个列表中。

要解决此问题，你可以按照以下步骤操作：

1. 创建一个 `collections.defaultdict`，将每个键的默认值设置为 `list`。
2. 使用 `dictionary.items()` 并结合循环，通过 `dict.append()` 将字典的值映射为键。
3. 使用 `dict()` 将 `collections.defaultdict` 转换为常规字典。

函数签名：`def invert_dictionary(obj: dict) -> dict:`

## 示例

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
