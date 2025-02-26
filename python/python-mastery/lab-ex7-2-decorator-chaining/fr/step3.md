# Plusieurs décorateurs et méthodes

Les choses peuvent devenir un peu problématiques lorsque les décorateurs sont appliqués à des méthodes dans une classe. Essayez d'appliquer votre décorateur `@logged` aux méthodes de la classe suivante.

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

Ça fonctionne-t-il du tout? (indice : non). Y a-t-il un moyen de corriger le code pour qu'il fonctionne? Par exemple, pouvez-vous le rendre fonctionnel pour l'exemple suivant?

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
