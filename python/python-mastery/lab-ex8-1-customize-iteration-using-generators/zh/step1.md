# 一个简单的生成器

如果你发现自己想要自定义迭代，那么你应该始终考虑生成器函数。它们很容易编写 —— 只需创建一个执行所需迭代逻辑并使用 `yield` 来发出值的函数即可。

例如，试试这个生成器，它允许你以分数步长遍历一系列数字（这是内置的 `range()` 函数不支持的）：

```python
>>> def frange(start,stop,step):
        while start < stop:
            yield start
            start += step

>>> for x in frange(0, 2, 0.25):
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```

对生成器进行迭代是一次性操作。例如，如果你尝试迭代两次会发生什么：

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

如果你想遍历相同的序列，则需要再次调用 `frange()` 来重新创建生成器。或者，你可以将所有内容打包到一个类中：

```python
>>> class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step

>>> f = FRange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```
