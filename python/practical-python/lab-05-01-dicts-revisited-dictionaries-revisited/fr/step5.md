# Instances et Classes

Les instances et les classes sont liées ensemble. L'attribut `__class__` renvoie à la classe.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

Le dictionnaire d'instance contient des données uniques à chaque instance, tandis que le dictionnaire de classe contient des données collectivement partagées par _toutes_ les instances.
