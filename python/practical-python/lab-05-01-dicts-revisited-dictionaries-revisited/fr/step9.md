# Comment l'héritage fonctionne

Les classes peuvent hériter d'autres classes.

```python
class A(B, C):
  ...
```

Les classes de base sont stockées dans un tuple dans chaque classe.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

Cela fournit un lien vers les classes parentes.
