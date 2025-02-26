# Lecture des attributs

Supposons que vous l lisez un attribut sur une instance.

```python
x = obj.name
```

L'attribut peut exister en deux endroits :

- Dans le dictionnaire d'instance local.
- Dans le dictionnaire de classe.

Les deux dictionnaires doivent être vérifiés. D'abord, vérifiez dans `__dict__` local. Si non trouvé, cherchez dans `__dict__` de la classe via `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Ce schéma de recherche est la manière dont les membres d'une _classe_ sont partagés par toutes les instances.
