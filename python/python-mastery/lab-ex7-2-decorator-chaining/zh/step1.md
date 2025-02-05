# 复制元数据

当一个函数被装饰器包装时，你通常会丢失有关函数名称、文档字符串和其他细节的信息。验证一下：

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... 查看输出...
>>>
```

修复 `logged` 装饰器的定义，使其能够正确复制函数元数据。为此，请按照注释中所示使用 `@wraps(func)` 装饰器。

完成后，确保装饰器保留函数名称和文档字符串。

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

修复你之前编写的 `@validated` 装饰器，使其也能使用 `@wraps(func)` 保留元数据。
