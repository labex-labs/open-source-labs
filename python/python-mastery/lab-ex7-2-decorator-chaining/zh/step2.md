# 你的第一个带参数的装饰器

你之前定义的 `@logged` 装饰器总是只打印一条包含函数名的简单消息。假设你希望用户能够指定某种自定义消息。

定义一个新的装饰器 `@logformat(fmt)`，它接受一个格式字符串作为参数，并使用 `fmt.format(func=func)` 将提供的函数格式化为一条日志消息：

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

为此，你需要定义一个接受参数的装饰器。测试时它应该是这样的：

```python
>>> import sample
为 add 添加日志记录
为 sub 添加日志记录
为 mul 添加日志记录
>>> sample.add(2,3)
调用 add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

为了进一步简化代码，展示如何使用 `@logformat` 装饰器来定义原来的 `@logged` 装饰器。
