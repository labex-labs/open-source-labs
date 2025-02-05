# “是一个”关系

继承建立了一种类型关系。

```python
class Shape:
  ...

class Circle(Shape):
  ...
```

检查对象实例。

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_重要提示：理想情况下，任何适用于父类实例的代码也将适用于子类实例。_
