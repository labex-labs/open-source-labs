# 练习 2.14：更多序列操作

交互式地试验一些序列归约操作。

```python
>>> data = [4, 9, 1, 25, 16, 100, 49]
>>> min(data)
1
>>> max(data)
100
>>> sum(data)
204
>>>
```

尝试遍历数据。

```python
>>> for x in data:
        print(x)

4
9
...
>>> for n, x in enumerate(data):
        print(n, x)

0 4
1 9
2 1
...
>>>
```

有时新手会在一些糟糕的代码片段中使用`for`语句、`len()`和`range()`，这些代码片段看起来就像是从一个生锈的 C 程序深处冒出来的。

```python
>>> for n in range(len(data)):
        print(data[n])

4
9
1
...
>>>
```

别这么做！不仅读起来会让每个人都眼睛难受，而且它在内存使用上效率低下，运行速度也慢得多。如果你想遍历数据，就用普通的`for`循环。如果你出于某种原因需要索引，就使用`enumerate()`。
