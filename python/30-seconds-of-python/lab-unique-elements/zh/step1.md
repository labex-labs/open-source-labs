# 列表中的唯一元素

编写一个名为 `unique_elements` 的 Python 函数，该函数以列表作为输入，并返回一个只包含唯一元素的新列表。你的函数应执行以下步骤：

- 从列表创建一个 `set` 以丢弃重复值。
- 从集合返回一个 `list`。

你的函数应具有以下签名：

```python
def unique_elements(li: List) -> List:
```

```python
def unique_elements(li):
  return list(set(li))
```

```python
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```
