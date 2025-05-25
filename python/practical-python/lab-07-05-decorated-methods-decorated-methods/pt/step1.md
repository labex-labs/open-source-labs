# Decoradores Predefinidos

Existem decoradores (decorators) predefinidos usados para especificar tipos especiais de métodos em definições de classe.

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

Vamos analisar cada um deles.
