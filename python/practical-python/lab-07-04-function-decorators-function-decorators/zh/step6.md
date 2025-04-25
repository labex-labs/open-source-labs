# 练习 7.10：用于计时的装饰器

如果你定义一个函数，它的名称和模块会存储在 `__name__` 和 `__module__` 属性中。例如：

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

在 `timethis.py` 文件中，编写一个装饰器函数 `timethis(func)`，它会在函数周围添加一层额外的逻辑，用于打印函数执行所需的时间。为此，你需要在函数调用前后添加计时代码，如下所示：

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

以下是你的装饰器应该如何工作的示例：

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

讨论：这个 `@timethis` 装饰器可以放在任何函数定义之前。因此，你可以将它用作性能调优的诊断工具。
