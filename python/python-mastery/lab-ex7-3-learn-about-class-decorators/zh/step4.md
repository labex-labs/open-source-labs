# 行转换

`Structure`类中缺少一个`from_row()`方法，该方法可使其与早期的CSV读取代码配合使用。我们来修复这个问题。给`Structure`类添加一个`_types`类变量和以下类方法：

```python
# structure.py

class Structure:
    _types = ()
 ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
 ...
```

修改`@validate_attributes`装饰器，使其检查各种验证器的`expected_type`属性，并使用它来填充上面的`_types`变量。

完成此操作后，你应该能够执行以下操作：

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
