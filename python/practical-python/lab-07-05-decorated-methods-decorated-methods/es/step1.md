# Decoradores predefinidos

Hay decoradores predefinidos que se utilizan para especificar tipos especiales de métodos en las definiciones de clases.

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

Vamos a ver uno por uno.
