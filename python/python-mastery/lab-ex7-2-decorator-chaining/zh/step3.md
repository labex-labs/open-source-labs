# 多个装饰器与方法

当装饰器应用于类中的方法时，情况可能会变得有点棘手。尝试将你的 `@logged` 装饰器应用于以下类中的方法。

```python
class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass
```

它甚至能正常工作吗？（提示：不能）有没有办法修复代码使其正常工作？例如，你能让以下示例正常工作吗？

```python
>>> s = Spam()
>>> s.instance_method()
instance_method
>>> Spam.class_method()
class_method
>>> Spam.static_method()
static_method
>>> s.property_method
property_method
>>>
```
