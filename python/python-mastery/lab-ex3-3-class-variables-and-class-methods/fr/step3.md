# Variables de classe et héritage

Dans cette étape, nous allons explorer comment les variables de classe interagissent avec l'héritage et en quoi elles peuvent servir de mécanisme de personnalisation. En Python, l'héritage permet à une sous - classe d'hériter d'attributs et de méthodes d'une classe de base. Les variables de classe sont des variables qui appartiennent à la classe elle - même, et non à une instance spécifique de la classe. Comprendre comment ces éléments fonctionnent ensemble est crucial pour créer un code flexible et maintenable.

## Variables de classe dans l'héritage

Lorsqu'une sous - classe hérite d'une classe de base, elle a automatiquement accès aux variables de classe de la classe de base. Cependant, une sous - classe peut remplacer (override) ces variables de classe. En faisant cela, la sous - classe peut modifier son comportement sans affecter la classe de base. C'est une fonctionnalité très puissante car elle vous permet de personnaliser le comportement d'une sous - classe selon vos besoins spécifiques.

## Création d'une classe Stock spécialisée

Créons une sous - classe de la classe `Stock`. Nous l'appellerons `DStock`, qui signifie Decimal Stock (Stock décimal). La principale différence entre `DStock` et la classe `Stock` normale est que `DStock` utilisera le type `Decimal` pour les valeurs de prix au lieu de `float`. Dans les calculs financiers, la précision est extrêmement importante, et le type `Decimal` offre des opérations arithmétiques décimales plus précises que le type `float`.

Pour créer cette sous - classe, nous allons créer un nouveau fichier nommé `decimal_stock.py`. Voici le code que vous devez placer dans ce fichier :

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

Après avoir créé le fichier `decimal_stock.py` avec le code ci - dessus, vous devez l'exécuter pour voir les résultats. Ouvrez votre terminal et suivez ces étapes :

```bash
cd ~/project
python decimal_stock.py
```

Vous devriez voir une sortie similaire à ceci :

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## Points clés sur les variables de classe et l'héritage

À partir de cet exemple, nous pouvons tirer plusieurs conclusions importantes :

1. La classe `DStock` hérite de toutes les méthodes de la classe `Stock`, comme la méthode `cost()`, sans avoir à les redéfinir. C'est l'un des principaux avantages de l'héritage, car cela vous évite d'écrire du code redondant.
2. En simplement remplaçant la variable de classe `types`, nous avons modifié la façon dont les données sont converties lors de la création de nouvelles instances de `DStock`. Cela montre comment les variables de classe peuvent être utilisées pour personnaliser le comportement d'une sous - classe.
3. La classe de base, `Stock`, reste inchangée et fonctionne toujours avec des valeurs de type `float`. Cela signifie que les modifications que nous avons apportées à la sous - classe n'affectent pas la classe de base, ce qui est un bon principe de conception.
4. La méthode de classe `from_row()` fonctionne correctement avec les classes `Stock` et `DStock`. Cela démontre la puissance de l'héritage, car la même méthode peut être utilisée avec différentes sous - classes.

Cet exemple montre clairement comment les variables de classe peuvent être utilisées comme mécanisme de configuration. Les sous - classes peuvent remplacer ces variables pour personnaliser leur comportement sans avoir à réécrire les méthodes.

## Discussion sur la conception

Considérons une approche alternative où nous plaçons les conversions de type dans la méthode `__init__` :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Avec cette approche, nous pouvons créer un objet `Stock` à partir d'une ligne de données comme ceci :

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

Bien que cette approche puisse sembler plus simple à première vue, elle présente plusieurs inconvénients :

1. Elle combine deux préoccupations différentes : l'initialisation de l'objet et la conversion des données. Cela rend le code plus difficile à comprendre et à maintenir.
2. La méthode `__init__` devient moins flexible car elle convertit toujours les entrées, même si elles sont déjà au bon type.
3. Elle restreint la façon dont les sous - classes peuvent personnaliser le processus de conversion. Les sous - classes auraient plus de difficulté à modifier la logique de conversion si elle est intégrée dans la méthode `__init__`.
4. Le code devient plus fragile. Si l'une des conversions échoue, l'objet ne peut pas être créé, ce qui peut entraîner des erreurs dans votre programme.

D'un autre côté, l'approche basée sur les méthodes de classe sépare ces préoccupations. Cela rend le code plus maintenable et flexible, car chaque partie du code a une seule responsabilité.
