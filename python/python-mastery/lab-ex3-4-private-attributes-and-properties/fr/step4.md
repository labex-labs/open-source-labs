# Ajout de `__slots__`

Modifiez votre nouvelle classe `Stock` pour utiliser `__slots__`. Vous allez constater que vous devrez utiliser un ensemble différent de noms d'attributs que précédemment - plus précisément, vous devrez lister les noms d'attributs privés (par exemple, si une propriété stocke une valeur dans un attribut `_shares`, c'est le nom que vous lisez dans `__slots__`). Vérifiez que la classe fonctionne toujours et que vous ne pouvez plus ajouter de nouveaux attributs.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' object has no attribute 'spam'
>>>
```
