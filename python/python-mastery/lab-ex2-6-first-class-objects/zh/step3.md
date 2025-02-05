# 重温内存

在 CTA 公交数据中，我们确定有 181 条唯一的公交路线。

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

问题：行程数据中包含多少个唯一的路线字符串对象？不要构建路线集合，而是构建对象 ID 的集合：

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

思考一下这个问题 —— 只有 181 个不同的路线名称，但生成的字典列表包含 542305 个不同的路线字符串。也许可以通过一些缓存或对象重用的方法来解决这个问题。事实证明，Python 有一个可用于缓存字符串的函数 `sys.intern()`。例如：

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

重启 Python 并尝试这个：

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

查看内存使用情况。

```python
>>> tracemalloc.get_traced_memory()
... 查看结果...
>>>
```

内存应该会大幅下降。观察：日期也存在大量重复。如果你也缓存日期字符串会发生什么？

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... 查看结果...
>>>
````
