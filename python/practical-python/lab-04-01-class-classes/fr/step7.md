# Exercice 4.1 : Objets en tant que structures de données

Dans les sections 2 et 3, nous avons travaillé avec des données représentées sous forme de tuples et de dictionnaires. Par exemple, une position d'action pourrait être représentée comme un tuple comme ceci :

```python
s = ('GOOG',100,490.10)
```

ou comme un dictionnaire comme ceci :

```python
s = { 'name'   : 'GOOG',
    'shares' : 100,
     'price'  : 490.10
}
```

Vous pouvez même écrire des fonctions pour manipuler de telles données. Par exemple :

```python
def cost(s):
    return s['shares'] * s['price']
```

Cependant, à mesure que votre programme grandit, vous pouvez vouloir créer une meilleure organisation. Ainsi, une autre approche pour représenter les données serait de définir une classe. Créez un fichier appelé `stock.py` et définissez une classe `Stock` qui représente une seule position d'action. Que les instances de `Stock` aient des attributs `name`, `shares` et `price`. Par exemple :

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

Créez quelques autres objets `Stock` et manipulez-les. Par exemple :

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... regardez la sortie...
>>>
```

Une chose à souligner ici est que la classe `Stock` fonctionne comme une usine pour créer des instances d'objets. Fondamentalement, vous l'appelez comme une fonction et elle crée un nouvel objet pour vous. De plus, il est important de souligner que chaque objet est distinct - chacun d'entre eux a ses propres données qui sont séparées des autres objets qui ont été créés.

Un objet défini par une classe est quelque peu similaire à un dictionnaire - juste avec une syntaxe un peu différente. Par exemple, au lieu d'écrire `s['name']` ou `s['price']`, vous écrivez maintenant `s.name` et `s.price`.
