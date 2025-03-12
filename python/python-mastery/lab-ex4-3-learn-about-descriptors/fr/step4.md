# Amélioration de l'implémentation des descripteurs

Dans cette étape, nous allons améliorer notre implémentation des descripteurs. Vous avez peut - être remarqué que dans certains cas, nous avons spécifié les noms de manière redondante. Cela peut rendre notre code un peu désordonné et plus difficile à maintenir. Pour résoudre ce problème, nous allons utiliser la méthode `__set_name__`, une fonctionnalité utile introduite en Python 3.6.

La méthode `__set_name__` est appelée automatiquement lorsque la classe est définie. Son principal rôle est de définir le nom du descripteur pour nous, de sorte que nous n'ayons pas à le faire manuellement à chaque fois. Cela rendra notre code plus propre et plus efficace.

Maintenant, mettons à jour votre fichier `validate.py` pour inclure la méthode `__set_name__`. Voici à quoi ressemblera le code mis à jour :

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

Dans le code ci - dessus, la méthode `__set_name__` de la classe `Validator` vérifie si l'attribut `name` est `None`. Si c'est le cas, elle définit `name` sur le nom de l'attribut réel utilisé dans la définition de la classe. De cette façon, nous n'avons pas besoin de spécifier le nom explicitement lors de la création d'instances des classes de descripteurs.

Maintenant que nous avons mis à jour le fichier `validate.py`, nous pouvons créer une version améliorée de notre classe `Stock`. Cette nouvelle version ne nous obligera pas à spécifier les noms de manière redondante. Voici le code de la classe `Stock` améliorée :

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

Dans cette classe `Stock`, nous créons simplement des instances des classes de descripteurs `String`, `PositiveInteger` et `PositiveFloat` sans spécifier les noms. La méthode `__set_name__` de la classe `Validator` s'occupera de définir les noms automatiquement.

Testons notre classe `Stock` améliorée. Tout d'abord, ouvrez votre terminal et accédez au répertoire du projet. Ensuite, exécutez le fichier `improved_stock.py` en mode interactif. Voici les commandes pour cela :

```bash
cd ~/project
python3 -i improved_stock.py
```

Une fois que vous êtes dans la session Python interactive, vous pouvez essayer les commandes suivantes pour tester la fonctionnalité de la classe `Stock` :

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

Ces commandes créent une instance de la classe `Stock`, affichent ses attributs, modifient la valeur d'un attribut, puis essaient de définir des valeurs invalides pour voir si les erreurs appropriées sont levées.

La méthode `__set_name__` définit automatiquement le nom du descripteur lorsque la classe est définie. Cela rend votre code plus propre et moins redondant, car vous n'avez plus besoin de spécifier le nom de l'attribut deux fois.

Cette amélioration démontre comment le protocole des descripteurs de Python continue d'évoluer, rendant plus facile l'écriture de code propre et maintenable.
