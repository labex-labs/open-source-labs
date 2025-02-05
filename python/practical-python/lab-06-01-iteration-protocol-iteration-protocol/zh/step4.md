# 练习6.1：迭代示例说明

创建以下列表：

```python
a = [1,9,4,25,16]
```

手动迭代这个列表。调用 `__iter__()` 获取一个迭代器，并调用 `__next__()` 方法获取连续的元素。

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

内置函数 `next()` 是调用迭代器的 `__next__()` 方法的快捷方式。尝试在文件上使用它：

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # 注意：这返回文件本身
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

持续调用 `next(f)`，直到到达文件末尾。观察会发生什么。
