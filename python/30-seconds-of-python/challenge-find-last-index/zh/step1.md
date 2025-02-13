# 找到最后一个匹配的索引

## 问题

编写一个函数 `find_last_index(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应返回 `lst` 中最后一个使 `fn` 返回 `True` 的元素的索引。如果没有元素满足该条件，函数应返回 `-1`。

## 示例

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
find_last_index([2, 4, 6, 8], lambda n: n % 2 == 1) # -1
```
