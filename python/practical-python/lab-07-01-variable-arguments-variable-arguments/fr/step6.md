# Exercice 7.2 : Passer des tuples et des dictionnaires en tant qu'arguments

Supposons que vous lisez des données à partir d'un fichier et que vous obteniez un tuple comme celui-ci :

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Maintenant, supposons que vous vouliez créer un objet `Stock` à partir de ces données. Si vous essayez de passer `data` directement, cela ne fonctionne pas :

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

Cela est facilement corrigé en utilisant `*data` à la place. Essayez ceci :

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Si vous avez un dictionnaire, vous pouvez utiliser `**` à la place. Par exemple :

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
