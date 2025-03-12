# Amélioration de la représentation des objets avec `__repr__`

En Python, les objets peuvent être représentés sous forme de chaînes de caractères de deux manières différentes. Ces représentations servent à des fins différentes et sont utiles dans diverses situations.

Le premier type est la **représentation sous forme de chaîne de caractères**. Elle est créée par la fonction `str()`, qui est appelée automatiquement lorsque vous utilisez la fonction `print()`. La représentation sous forme de chaîne de caractères est conçue pour être lisible par l'homme. Elle présente l'objet dans un format que nous pouvons facilement comprendre et interpréter.

Le deuxième type est la **représentation sous forme de code**. Elle est générée par la fonction `repr()`. La représentation sous forme de code montre le code que vous devriez écrire pour recréer l'objet. Elle vise plus à fournir un moyen précis et non ambigu de représenter l'objet dans le code.

Regardons un exemple concret en utilisant la classe `date` intégrée à Python. Cela vous aidera à voir la différence entre les représentations sous forme de chaîne de caractères et de code en action.

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

Dans cet exemple, lorsque nous utilisons `print(d)`, Python appelle la fonction `str()` sur l'objet `date` `d`, et nous obtenons une date lisible par l'homme au format `AAAA-MM-JJ`. Lorsque nous tapons simplement `d` dans le shell interactif, Python appelle la fonction `repr()`, et nous voyons le code nécessaire pour recréer l'objet `date`.

Vous pouvez obtenir explicitement la chaîne de caractères retournée par `repr()` de diverses manières. Voici quelques exemples :

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

Maintenant, appliquons ce concept à notre classe `Stock`. Nous allons améliorer la classe en implémentant la méthode `__repr__`. Cette méthode spéciale est appelée par Python lorsqu'il a besoin de la représentation sous forme de code d'un objet.

Pour ce faire, ouvrez le fichier `stock.py` dans votre éditeur. Ensuite, ajoutez la méthode `__repr__` à la classe `Stock`. La méthode `__repr__` doit retourner une chaîne de caractères qui montre le code nécessaire pour recréer l'objet `Stock`.

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Après avoir ajouté la méthode `__repr__`, votre classe `Stock` complète devrait maintenant ressembler à ceci :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Maintenant, testons notre classe `Stock` modifiée. Ouvrez un shell interactif Python en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Une fois le shell interactif ouvert, essayez les commandes suivantes :

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

Vous pouvez également voir comment la méthode `__repr__` fonctionne avec un portefeuille d'actions. Voici un exemple :

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

Comme vous pouvez le voir, la méthode `__repr__` a rendu nos objets `Stock` beaucoup plus informatifs lorsqu'ils sont affichés dans le shell interactif ou le débogueur. Elle montre maintenant le code nécessaire pour recréer chaque objet, ce qui est très utile pour le débogage et la compréhension de l'état des objets.

Une fois que vous avez terminé les tests, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
>>> exit()
```
