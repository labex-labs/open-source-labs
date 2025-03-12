# Amélioration des classes avec des capacités d'itération

Maintenant, nous avons rendu notre classe `Structure` et ses sous - classes compatibles avec l'itération. L'itération est un concept puissant en Python qui vous permet de parcourir une collection d'éléments un par un. Lorsqu'une classe prend en charge l'itération, elle devient plus flexible et peut fonctionner avec de nombreuses fonctionnalités intégrées de Python. Explorons comment cette prise en charge de l'itération permet d'utiliser de nombreuses fonctionnalités puissantes en Python.

## Exploitation de l'itération pour les conversions de séquences

En Python, il existe des fonctions intégrées telles que `list()` et `tuple()`. Ces fonctions sont très utiles car elles peuvent prendre n'importe quel objet itérable en entrée. Un objet itérable est quelque chose sur lequel vous pouvez itérer, comme une liste, un tuple, ou maintenant, les instances de notre classe `Structure`. Étant donné que notre classe `Structure` prend maintenant en charge l'itération, nous pouvons facilement convertir ses instances en listes ou en tuples.

1. Essayons ces opérations avec une instance de `Stock`. La classe `Stock` est une sous - classe de `Structure`. Exécutez la commande suivante dans votre terminal :

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

Cette commande importe d'abord la classe `Stock`, crée une instance de celle - ci, puis convertit cette instance en une liste et en un tuple à l'aide des fonctions `list()` et `tuple()` respectivement. La sortie vous montrera l'instance représentée sous forme de liste et de tuple :

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## Désempilement (Unpacking)

Python a une fonctionnalité très utile appelée désempilement (unpacking). Le désempilement vous permet de prendre un objet itérable et d'affecter ses éléments à des variables individuelles en une seule opération. Étant donné que notre instance de `Stock` est itérable, nous pouvons utiliser cette fonctionnalité de désempilement sur elle.

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

Dans ce code, nous créons une instance de `Stock` puis nous désempilons ses éléments dans trois variables : `name`, `shares` et `price`. Ensuite, nous affichons ces variables. La sortie montrera les valeurs de ces variables :

```
Name: GOOG, Shares: 100, Price: 490.1
```

## Ajout de capacités de comparaison

Lorsqu'une classe prend en charge l'itération, il devient plus facile d'implémenter des opérations de comparaison. Les opérations de comparaison sont utilisées pour vérifier si deux objets sont égaux ou non. Ajoutons une méthode `__eq__()` à notre classe `Structure` pour comparer les instances.

1. Ouvrez à nouveau le fichier `structure.py`. La méthode `__eq__()` est une méthode spéciale en Python qui est appelée lorsque vous utilisez l'opérateur `==` pour comparer deux objets. Ajoutez le code suivant à la classe `Structure` dans le fichier `structure.py` :

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

Cette méthode vérifie d'abord si l'objet `other` est une instance de la même classe que `self` à l'aide de la fonction `isinstance()`. Ensuite, elle convertit à la fois `self` et `other` en tuples et vérifie si ces tuples sont égaux.

Le fichier `structure.py` complet devrait maintenant ressembler à ceci :

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. Après avoir ajouté la méthode `__eq__()`, enregistrez le fichier `structure.py`.

3. Testons la capacité de comparaison. Exécutez la commande suivante dans votre terminal :

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

Ce code crée trois instances de `Stock` : `a`, `b` et `c`. Ensuite, il compare `a` avec `b` et `a` avec `c` à l'aide de l'opérateur `==`. La sortie montrera les résultats de ces comparaisons :

```
a == b: True
a == c: False
```

4. Maintenant, pour nous assurer que tout fonctionne correctement, nous devons exécuter les tests unitaires. Les tests unitaires sont un ensemble de code qui vérifie si différentes parties de votre programme fonctionnent comme prévu. Exécutez la commande suivante dans votre terminal :

```bash
python3 teststock.py
```

Si tout fonctionne correctement, vous devriez voir une sortie indiquant que les tests ont réussi :

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

En ajoutant seulement deux méthodes simples (`__iter__()` et `__eq__()`), nous avons considérablement amélioré notre classe `Structure` avec des capacités qui la rendent plus "Pythonique" et plus facile à utiliser.
