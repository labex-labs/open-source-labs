# 迭代：协议

考虑 `for` 语句。

```python
for x in obj:
    # 语句
```

在底层发生了什么？

```python
_iter = obj.__iter__()        # 获取迭代器对象
while True:
    try:
        x = _iter.__next__()  # 获取下一个元素
        # 语句...
    except StopIteration:     # 没有更多元素
        break
```

所有与 `for` 循环配合使用的对象都实现了这个底层迭代协议。

示例：手动迭代列表。

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```
