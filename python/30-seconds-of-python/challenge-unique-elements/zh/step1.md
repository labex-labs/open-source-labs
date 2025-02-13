# 列表中的唯一元素

## 问题

编写一个名为 `unique_elements` 的 Python 函数，该函数接受一个列表作为输入，并返回一个只包含唯一元素的新列表。你的函数应执行以下步骤：

- 从列表创建一个 `set` 以丢弃重复的值。
- 从集合返回一个 `list`。

你的函数应具有以下签名：

```python
def unique_elements(li: List) -> List:
```

## 示例

```python
assert unique_elements([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]
assert unique_elements(['a', 'b', 'c', 'a', 'd']) == ['a', 'b', 'c', 'd']
assert unique_elements([]) == []
```
