# 找到匹配的索引

## 问题

编写一个函数 `find_index(lst, fn)`，它接受一个列表 `lst` 和一个测试函数 `fn` 作为参数。该函数应返回 `lst` 中第一个使 `fn` 返回 `True` 的元素的索引。

## 示例

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
