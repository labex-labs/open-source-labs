# Application des validateurs à une classe Stock

Dans cette étape, nous allons voir comment nos validateurs fonctionnent dans une situation réelle. Les validateurs sont comme de petits vérificateurs qui s'assurent que les données que nous utilisons respectent certaines règles. Nous allons créer une classe `Stock`. Une classe est comme un modèle pour créer des objets. Dans ce cas, la classe `Stock` représentera une action boursière, et nous utiliserons nos validateurs pour nous assurer que les valeurs de ses attributs (comme le nombre de parts et le prix) sont valides.

## Création de la classe Stock

Tout d'abord, nous devons créer un nouveau fichier. Dans le WebIDE, créez un nouveau fichier appelé `stock.py`. Ce fichier contiendra le code de notre classe `Stock`. Maintenant, ajoutez le code suivant au fichier `stock.py` :

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

Analysons ce que fait ce code :

1. Nous commençons par importer les validateurs `PositiveInteger` et `PositiveFloat` depuis notre module `validate`. Ces validateurs nous aideront à nous assurer que le nombre de parts est un entier positif et que le prix est un nombre à virgule flottante positif.
2. Ensuite, nous définissons une classe `Stock`. À l'intérieur de la classe, nous avons une méthode `__init__`. Cette méthode est appelée lorsque nous créons un nouvel objet `Stock`. Elle prend trois paramètres : `name`, `shares` et `price`, et les assigne aux attributs de l'objet.
3. Nous utilisons des propriétés (properties) et des mutateurs (setters) pour valider les valeurs de `shares` et `price`. Une propriété est un moyen de contrôler l'accès à un attribut, et un mutateur est une méthode qui est appelée lorsque nous essayons de définir la valeur de cet attribut. Lorsque nous définissons l'attribut `shares`, la méthode `PositiveInteger.check` est appelée pour nous assurer que la valeur est un entier positif. De même, lorsque nous définissons l'attribut `price`, la méthode `PositiveFloat.check` est appelée pour nous assurer que la valeur est un nombre à virgule flottante positif.
4. Enfin, nous avons une méthode `cost`. Cette méthode calcule le coût total de l'action en multipliant le nombre de parts par le prix.

## Test de la classe Stock

Maintenant que nous avons créé notre classe `Stock`, nous devons la tester pour voir si les validateurs fonctionnent correctement. Ouvrez un nouveau terminal et lancez l'interpréteur Python. Vous pouvez le faire en exécutant la commande suivante :

```bash
python3
```

Une fois que l'interpréteur Python est en cours d'exécution, nous pouvons importer et tester notre classe `Stock`. Entrez le code suivant dans l'interpréteur Python :

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

Lorsque vous exécutez ce code, vous devriez voir une sortie similaire à ceci :

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

Cette sortie montre que nos validateurs fonctionnent comme prévu. La classe `Stock` ne nous permet pas de définir des valeurs invalides pour `shares` et `price`. Lorsque nous essayons de définir une valeur invalide, une erreur est levée, et nous pouvons capturer et afficher cette erreur.

## Comprendre l'aide de l'héritage

L'un des grands avantages de l'utilisation de nos validateurs est que nous pouvons facilement combiner différentes règles de validation. L'héritage est un concept puissant en Python qui nous permet de créer de nouvelles classes basées sur des classes existantes. Avec l'héritage multiple, nous pouvons utiliser la fonction `super()` pour appeler des méthodes de plusieurs classes parentes.

Par exemple, si nous voulons nous assurer que le nom de l'action n'est pas vide, nous pouvons suivre ces étapes :

1. Importer le validateur `NonEmptyString` depuis le module `validate`. Ce validateur nous aidera à vérifier si le nom de l'action n'est pas une chaîne de caractères vide.
2. Ajouter un mutateur de propriété pour l'attribut `name` dans la classe `Stock`. Ce mutateur utilisera la méthode `NonEmptyString.check()` pour valider le nom de l'action.

Cela montre comment l'héritage, en particulier l'héritage multiple avec la fonction `super()`, nous permet de construire des composants flexibles et réutilisables dans différentes combinaisons.

Lorsque vous avez terminé de tester, vous pouvez quitter l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```
