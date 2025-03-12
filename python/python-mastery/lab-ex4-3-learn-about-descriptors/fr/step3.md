# Mise en œuvre de validateurs à l'aide de descripteurs

Dans cette étape, nous allons créer un système de validation à l'aide de descripteurs. Mais d'abord, comprenons ce que sont les descripteurs et pourquoi nous les utilisons. Les descripteurs sont des objets Python qui implémentent le protocole des descripteurs, qui inclut les méthodes `__get__`, `__set__` ou `__delete__`. Ils vous permettent de personnaliser la manière dont un attribut est accédé, défini ou supprimé sur un objet. Dans notre cas, nous utiliserons les descripteurs pour créer un système de validation qui garantit l'intégrité des données. Cela signifie que les données stockées dans nos objets respecteront toujours certains critères, comme être d'un type spécifique ou avoir une valeur positive.

Maintenant, commençons à créer notre système de validation. Nous allons créer un nouveau fichier appelé `validate.py` dans le répertoire du projet. Ce fichier contiendra les classes qui implémentent nos validateurs.

```python
# validate.py

class Validator:
    def __init__(self, name):
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

Dans le fichier `validate.py`, nous définissons d'abord une classe de base appelée `Validator`. Cette classe a une méthode `__init__` qui prend un paramètre `name`, qui sera utilisé pour identifier l'attribut en cours de validation. La méthode `check` est une méthode de classe qui renvoie simplement la valeur passée à elle. La méthode `__set__` est une méthode de descripteur qui est appelée lorsqu'un attribut est défini sur un objet. Elle appelle la méthode `check` pour valider la valeur, puis stocke la valeur validée dans le dictionnaire de l'objet.

Nous définissons ensuite trois sous - classes de `Validator` : `String`, `PositiveInteger` et `PositiveFloat`. Chacune de ces sous - classes remplace la méthode `check` pour effectuer des vérifications de validation spécifiques. La classe `String` vérifie si la valeur est une chaîne de caractères, la classe `PositiveInteger` vérifie si la valeur est un entier positif, et la classe `PositiveFloat` vérifie si la valeur est un nombre positif (soit un entier, soit un flottant).

Maintenant que nous avons défini nos validateurs, modifions notre classe `Stock` pour utiliser ces validateurs. Nous allons créer un nouveau fichier appelé `stock_with_validators.py` et importer les validateurs depuis le fichier `validate.py`.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

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

Dans le fichier `stock_with_validators.py`, nous définissons la classe `Stock` et utilisons les validateurs comme attributs de classe. Cela signifie que chaque fois qu'un attribut est défini sur un objet `Stock`, la méthode `__set__` du validateur correspondant sera appelée pour valider la valeur. La méthode `__init__` initialise les attributs de l'objet `Stock`, et les méthodes `cost`, `sell` et `__repr__` fournissent des fonctionnalités supplémentaires.

Maintenant, testons notre classe `Stock` basée sur des validateurs. Nous allons ouvrir un terminal, accéder au répertoire du projet et exécuter le fichier `stock_with_validators.py` en mode interactif.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Une fois que l'interpréteur Python est en cours d'exécution, nous pouvons essayer quelques commandes pour tester le système de validation.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

Dans le code de test, nous créons d'abord un objet `Stock` avec des valeurs valides et affichons ses attributs pour vérifier qu'ils sont correctement définis. Nous essayons ensuite de changer l'attribut `shares` pour une valeur valide et l'affichons à nouveau pour confirmer le changement. Enfin, nous essayons de définir l'attribut `shares` sur une valeur invalide (une chaîne de caractères et un nombre négatif) et capturons les exceptions levées par les validateurs.

Remarquez à quel point notre code est maintenant beaucoup plus propre. La classe `Stock` n'a plus besoin d'implémenter toutes ces méthodes de propriétés - les validateurs gèrent toutes les vérifications de type et les contraintes.

Les descripteurs nous ont permis de créer un système de validation réutilisable qui peut être appliqué à n'importe quel attribut de classe. C'est un modèle puissant pour maintenir l'intégrité des données dans toute votre application.
