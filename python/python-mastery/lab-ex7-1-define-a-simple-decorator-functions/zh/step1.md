# 你的第一个装饰器

为了开始学习装饰器，编写一个非常简单的装饰器函数，每次调用函数时简单地打印一条消息。创建一个文件`logcall.py`并定义以下函数：

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

现在，创建一个单独的文件`sample.py`，并将其应用于几个函数定义：

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

按如下方式测试你的代码：

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
