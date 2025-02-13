# 找到匹配值

## 问题

编写一个名为 `find(lst, fn)` 的函数，该函数接受一个列表 `lst` 和一个测试函数 `fn` 作为参数。该函数应返回 `lst` 中第一个使 `fn` 返回 `True` 的元素的值。如果没有元素满足测试函数，该函数应返回 `None`。

## 示例

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```
