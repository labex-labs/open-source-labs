# 预定义装饰器

在类定义中，有一些预定义的装饰器用于指定特殊类型的方法。

```python
class Foo:
    def bar(self,a):
     ...

    @staticmethod
    def spam(a):
     ...

    @classmethod
    def grok(cls,a):
     ...

    @property
    def name(self):
     ...
```

让我们逐个来看。
