# Exercice 2.17 : Inversion d'un dictionnaire

Un dictionnaire associe des clés à des valeurs. Par exemple, un dictionnaire de prix d'actions.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

Si vous utilisez la méthode `items()`, vous pouvez obtenir des paires `(clé,valeur)` :

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

Cependant, que se passe-t-il si vous voulez obtenir une liste de paires `(valeur, clé)` à la place? _Indice : utilisez `zip()`._

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Pourquoi feriez-vous cela? Pour commencer, cela vous permet de réaliser certains types de traitement de données sur les données du dictionnaire.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

Cela illustre également une caractéristique importante des tuples. Lorsqu'ils sont utilisés dans des comparaisons, les tuples sont comparés élément par élément, en commençant par le premier élément. De la même manière que les chaînes de caractères sont comparées caractère par caractère.

`zip()` est souvent utilisé dans des situations comme celle-ci où vous devez associer des données provenant de différents emplacements. Par exemple, en associant les noms de colonnes aux valeurs de colonne afin de créer un dictionnaire de valeurs nommées.

Notez que `zip()` n'est pas limité à des paires. Par exemple, vous pouvez l'utiliser avec n'importe quel nombre de listes d'entrée :

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

De plus, sachez que `zip()` s'arrête une fois que la plus courte séquence d'entrée est épuisée.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```
