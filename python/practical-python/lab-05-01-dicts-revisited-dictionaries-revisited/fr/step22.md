# Exercice 5.5 : Héritage

Créez une nouvelle classe qui hérite de `Stock`.

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

L'héritage est implémenté en étendant le processus de recherche d'attributs. L'attribut `__bases__` a un tuple des parents directs :

```python
>>> NewStock.__bases__
(<class'stock.Stock'>,)
>>>
```

L'attribut `__mro__` a un tuple de tous les parents, dans l'ordre dans lequel ils seront recherchés pour des attributs.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class'stock.Stock'>, <class 'object'>)
>>>
```

Voici comment la méthode `cost()` de l'instance `n` ci-dessus serait trouvée :

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```
