# 契约式编程

也称为契约式设计，大量使用断言是一种设计软件的方法。它规定软件设计师应为软件组件定义精确的接口规范。

例如，你可以在函数的所有输入上设置断言。

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

检查输入将立即捕获未使用适当参数的调用者。

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
