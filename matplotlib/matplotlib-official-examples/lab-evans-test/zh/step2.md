# 创建一个自定义单位类

在这一步中，我们将创建一个自定义单位类——`Foo`。这个类将支持转换以及根据“单位”进行不同的刻度格式化。这里，“单位”仅仅是一个标量转换因子。

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
