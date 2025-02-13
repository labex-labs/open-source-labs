# 深度扁平化列表

## 问题

编写一个函数 `deep_flatten(lst)`，它接受一个列表 `lst` 作为参数，并返回一个新的列表，该列表是 `lst` 的深度扁平化版本。该函数应使用递归以及 `isinstance()` 函数和 `collections.abc.Iterable` 来检查一个元素是否可迭代。如果一个元素是可迭代的，该函数应递归地对该元素应用 `deep_flatten()`。否则，该函数应返回一个只包含该元素的列表。

## 示例

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```
