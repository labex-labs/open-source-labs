# 准备工作

回顾练习4.3，你创建了一系列`Validator`类来执行不同类型的类型和值检查。例如：

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

你可以在函数中像这样使用验证器：

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

在本练习中，我们将更进一步。
