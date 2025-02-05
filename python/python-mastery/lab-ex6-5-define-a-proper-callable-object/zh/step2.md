# 创建可调用对象

在`validate.py`文件中，先创建一个如下的类：

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

通过将其应用于一个函数来测试这个类：

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Calling <function add at 0x1014df598>
5
>>>
```
