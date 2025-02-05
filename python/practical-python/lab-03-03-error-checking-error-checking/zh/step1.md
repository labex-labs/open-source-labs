# 程序如何出错

Python 不会对函数参数的类型或值进行任何检查或验证。函数可以处理任何与函数中的语句兼容的数据。

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

如果函数中存在错误，它们会在运行时出现（作为异常）。

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

为了验证代码，非常强调测试（稍后介绍）。
