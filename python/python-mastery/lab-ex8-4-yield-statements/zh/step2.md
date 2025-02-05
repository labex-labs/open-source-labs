# 引发异常

在 `cofollow.py` 文件中，你创建了一个协程 `printer()`。修改代码以捕获并报告异常，如下所示：

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

现在，尝试一个实验：

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERROR: ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

注意正在运行的生成器如何不会因异常而终止。这仅仅是允许 `yield` 语句发出错误信号，而不是接收值。
