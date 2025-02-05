# 实现日志记录的代码

也许你可以创建一个函数，用于生成添加了日志记录功能的函数。也就是一个包装器。

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

现在使用它。

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

当你调用由 `logged` 返回的函数时会发生什么？

```python
logged_add(3, 4)      # 你会看到日志消息出现
```

这个示例展示了创建所谓的 **包装器函数** 的过程。

包装器是一个围绕另一个函数的函数，它带有一些额外的处理步骤，但在其他方面与原始函数的工作方式完全相同。

```python
>>> logged_add(3, 4)
Calling add   # 额外的输出。由包装器添加
7
>>>
```

**注意**：`logged()` 函数创建包装器并将其作为结果返回。
