# 使用 getattr()

`getattr()` 函数对于编写以极其通用的方式处理对象的代码非常有用。为了说明这一点，考虑以下示例，它会打印出一组用户定义的属性：

```python
>>> s= Stock('GOOG', 100, 490.1)
>>> fields = ['name','shares','price']
>>> for name in fields:
           print(name, getattr(s, name))

name GOOG
shares 100
price 490.1
>>>
```
