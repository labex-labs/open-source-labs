# 强制检查

修改`ValidatedFunction`类，使其能够执行通过函数注释附加的值检查。例如：

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

提示：要做到这一点，可以尝试使用签名绑定。使用`Signature`对象的`bind()`方法将函数参数绑定到参数名称。然后将此信息与`__annotations__`属性进行交叉引用，以获取不同的验证器类。

请记住，你正在创建一个看起来像函数的对象，但实际上它不是。幕后有一些神奇的操作在进行。
