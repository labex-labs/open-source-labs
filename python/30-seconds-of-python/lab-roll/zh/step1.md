# 旋转列表元素

编写一个函数 `roll(lst, offset)`，它接受一个列表 `lst` 和一个整数 `offset`。该函数应将指定数量的元素移动到列表的开头。如果 `offset` 为正数，元素应从列表末尾移动到开头。如果 `offset` 为负数，元素应从列表开头移动到末尾。

返回修改后的列表。

```python
def roll(lst, offset):
  return lst[-offset:] + lst[:-offset]
```

```python
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
