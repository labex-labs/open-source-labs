# 检查函数

定义一个简单的函数：

```python
>>> def add(x,y):
       'Adds two things'
       return x+y

>>>
```

对该函数执行 `dir()` 来查看其属性。

```python
>>> dir(add)
... 查看结果...
>>>
```

获取一些基本信息，如函数名、定义模块名和文档字符串。

```python
>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>> add.__doc__
'Adds two things'
>>>
```

函数的 `__code__` 属性包含有关函数实现的底层信息。看看你能否查看这个属性并确定所需参数的数量和局部变量的名称。
