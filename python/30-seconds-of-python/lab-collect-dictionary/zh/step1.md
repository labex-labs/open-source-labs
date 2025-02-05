# 反转字典

编写一个函数 `invert_dictionary(obj)`，它接受一个字典 `obj` 作为输入，并返回一个键值颠倒的新字典。输入字典将具有非唯一的可哈希值。如果两个或更多键具有相同的值，该函数应将这些键追加到输出字典中的一个列表中。

要解决这个问题，你可以按照以下步骤进行：

1. 创建一个 `collections.defaultdict`，将每个键的默认值设为列表。
2. 使用 `dictionary.items()` 并结合循环，通过 `dict.append()` 将字典的值映射为键。
3. 使用 `dict()` 将 `collections.defaultdict` 转换为常规字典。

函数签名：`def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
