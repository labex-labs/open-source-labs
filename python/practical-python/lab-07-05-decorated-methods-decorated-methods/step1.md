# Predefined Decorators

There are predefined decorators used to specify special kinds of methods in class definitions.

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

Let's go one by one.
