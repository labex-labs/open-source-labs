# Élimination des noms de propriétés avec les descripteurs (Descriptors)

Dans l'étape précédente, lors de la création de propriétés typées, nous devions explicitement indiquer les noms des propriétés. Cela est redondant car les noms des propriétés sont déjà spécifiés dans la définition de la classe. Dans cette étape, nous allons utiliser des descripteurs pour éliminer ce redondance.

Un descripteur en Python est un objet spécial qui contrôle la manière dont l'accès aux attributs fonctionne. Lorsque vous implémentez la méthode `__set_name__` dans un descripteur, il peut automatiquement récupérer le nom de l'attribut à partir de la définition de la classe.

Commençons par créer un nouveau fichier.

1. Créez un nouveau fichier nommé `improved_typedproperty.py` avec le code suivant :

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

Ce code définit une classe de descripteur appelée `TypedProperty` qui vérifie le type des valeurs assignées aux attributs. La méthode `__set_name__` est appelée automatiquement lorsque le descripteur est assigné à un attribut de classe. Cela permet au descripteur de capturer le nom de l'attribut sans que nous ayons à le spécifier manuellement.

Ensuite, nous allons créer une classe qui utilise ces propriétés typées améliorées.

2. Créez un nouveau fichier nommé `stock_improved.py` qui utilise les propriétés typées améliorées :

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Remarquez que nous n'avons plus besoin de spécifier les noms des propriétés lors de la création des propriétés typées. Le descripteur récupérera automatiquement le nom de l'attribut à partir de la définition de la classe.

Maintenant, testons notre classe améliorée.

3. Créez un fichier de test `test_stock_improved.py` pour tester la version améliorée :

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Enfin, nous allons exécuter le test pour voir si tout fonctionne comme prévu.

4. Exécutez le test :

```bash
python3 test_stock_improved.py
```

Vous devriez voir une sortie similaire à :

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

Dans cette étape, nous avons amélioré notre système de vérification de type en utilisant des descripteurs et la méthode `__set_name__`. Cela élimine la spécification redondante des noms de propriétés, rendant le code plus court et moins sujet aux erreurs.

La méthode `__set_name__` est une fonctionnalité très utile des descripteurs. Elle leur permet de recueillir automatiquement des informations sur la manière dont ils sont utilisés dans une définition de classe. Cela peut être utilisé pour créer des API plus faciles à comprendre et à utiliser.
