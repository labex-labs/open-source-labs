# Décorateurs prédéfinis

Il existe des décorateurs prédéfinis utilisés pour spécifier des types spéciaux de méthodes dans les définitions de classes.

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

Allons-y un par un.
