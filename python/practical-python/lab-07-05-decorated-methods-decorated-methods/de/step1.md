# Vordefinierte Dekoratoren

Es gibt vordefinierte Dekoratoren, die verwendet werden, um spezielle Arten von Methoden in Klassendefinitionen anzugeben.

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

Gehen wir nacheinander durch.
