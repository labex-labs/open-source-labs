# Rendre les objets comparables avec `__eq__`

En Python, lorsque vous utilisez l'opérateur `==` pour comparer deux objets, Python appelle en réalité la méthode spéciale `__eq__`. Par défaut, cette méthode compare les identités des objets, ce qui signifie qu'elle vérifie si ils sont stockés à la même adresse mémoire, plutôt que de comparer leur contenu.

Regardons un exemple. Supposons que nous ayons une classe `Stock`, et que nous créons deux objets `Stock` avec les mêmes valeurs. Ensuite, nous essayons de les comparer en utilisant l'opérateur `==`. Voici comment vous pouvez le faire dans l'interpréteur Python :

Tout d'abord, lancez l'interpréteur Python en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Ensuite, dans l'interpréteur Python, exécutez le code suivant :

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

Comme vous pouvez le voir, même si les deux objets `Stock` `a` et `b` ont les mêmes valeurs pour leurs attributs (`name`, `shares` et `price`), Python les considère comme des objets différents car ils sont stockés à des emplacements mémoire différents.

Pour résoudre ce problème, nous pouvons implémenter la méthode `__eq__` dans notre classe `Stock`. Cette méthode sera appelée chaque fois que l'opérateur `==` est utilisé sur des objets de la classe `Stock`.

Maintenant, réouvrez le fichier `stock.py`. À l'intérieur de la classe `Stock`, ajoutez la méthode `__eq__` suivante :

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

Analysons ce que fait cette méthode :

1. Tout d'abord, elle utilise la fonction `isinstance` pour vérifier si l'objet `other` est une instance de la classe `Stock`. Cela est important car nous voulons seulement comparer des objets `Stock` avec d'autres objets `Stock`.
2. Si `other` est un objet `Stock`, elle compare ensuite les attributs (`name`, `shares` et `price`) de l'objet `self` et de l'objet `other`.
3. Elle retourne `True` seulement si les deux objets sont des instances de `Stock` et que leurs attributs sont identiques.

Après avoir ajouté la méthode `__eq__`, votre classe `Stock` complète devrait ressembler à ceci :

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

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Maintenant, testons notre classe `Stock` améliorée. Relancez l'interpréteur Python :

```bash
python3
```

Ensuite, exécutez le code suivant dans l'interpréteur Python :

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

Parfait ! Maintenant, nos objets `Stock` peuvent être correctement comparés en fonction de leur contenu, plutôt que de leur adresse mémoire.

La vérification `isinstance` dans la méthode `__eq__` est cruciale. Elle garantit que nous ne comparons que des objets `Stock`. Si nous n'avions pas cette vérification, comparer un objet `Stock` avec quelque chose qui n'est pas un objet `Stock` pourrait générer des erreurs.

Une fois que vous avez terminé les tests, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
>>> exit()
```
