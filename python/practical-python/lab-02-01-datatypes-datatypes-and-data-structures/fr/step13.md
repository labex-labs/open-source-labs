# Exercice 2.3 : Quelques autres opérations sur les dictionnaires

Si vous convertissez un dictionnaire en une liste, vous obtiendrez toutes ses clés :

```python
>>> list(d)
['name','shares', 'price', 'date', 'account']
>>>
```

De manière similaire, si vous utilisez l'instruction `for` pour itérer sur un dictionnaire, vous obtiendrez les clés :

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Essayez cette variante qui effectue une recherche en même temps :

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

Vous pouvez également obtenir toutes les clés en utilisant la méthode `keys()` :

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name','shares', 'price', 'date', 'account'])
>>>
```

`keys()` est un peu particulier car elle renvoie un objet `dict_keys` spécial.

C'est une couche sur le dictionnaire original qui vous donne toujours les clés actuelles - même si le dictionnaire change. Par exemple, essayez ceci :

```python
>>> del d['account']
>>> keys
dict_keys(['name','shares', 'price', 'date'])
>>>
```

Remarquez attentivement que `'account'` est disparu de `keys` même si vous n'avez pas appelé `d.keys()` à nouveau.

Une manière plus élégante de travailler avec les clés et les valeurs en même temps est d'utiliser la méthode `items()`. Cela vous donne des tuples `(clé, valeur)` :

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

Si vous avez des tuples tels que `items`, vous pouvez créer un dictionnaire en utilisant la fonction `dict()`. Essayez :

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
