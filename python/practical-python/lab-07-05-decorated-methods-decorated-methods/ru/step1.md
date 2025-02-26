# Предопределенные декораторы

Существуют предопределенные декораторы, которые используются для указания особых типов методов в определениях классов.

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

Рассмотрим их по порядку.
