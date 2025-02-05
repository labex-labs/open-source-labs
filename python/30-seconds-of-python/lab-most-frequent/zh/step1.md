# 出现频率最高的元素

编写一个名为 `most_frequent(lst)` 的Python函数，该函数接受一个整数列表作为输入，并返回列表中出现频率最高的元素。如果有多个元素出现的次数相同且频率最高，则返回列表中最先出现的那个元素。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `set()` 获取 `lst` 中的唯一值。
2. 使用 `max()` 找到出现次数最多的元素。

你的函数应该具有以下签名：

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
