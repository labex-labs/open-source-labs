# 列表排序

列表可以进行“原地”排序。

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# 逆序
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# 它适用于任何有序数据
s = ['foo', 'bar','spam']
s.sort()                    # ['bar', 'foo','spam']
```

如果你想创建一个新的已排序列表，可以使用 `sorted()`：

```python
t = sorted(s)               # s 不变，t 包含已排序的值
```
