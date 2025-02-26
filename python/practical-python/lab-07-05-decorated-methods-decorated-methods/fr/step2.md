# Méthodes statiques

`@staticmethod` est utilisé pour définir une soi-disant méthode de classe _statique_ (du C++/Java). Une méthode statique est une fonction qui fait partie de la classe, mais qui _ne_ fonctionne _pas_ sur les instances.

```python
class Foo(object):
    @staticmethod
    def bar(x):
        print('x =', x)

>>> Foo.bar(2) # x=2
>>>
```

Les méthodes statiques sont parfois utilisées pour implémenter le code d'assistance interne pour une classe. Par exemple, le code pour aider à gérer les instances créées (gestion de la mémoire, ressources système, persistance, verrouillage, etc.). Elles sont également utilisées par certains patrons de conception (non discutés ici).
