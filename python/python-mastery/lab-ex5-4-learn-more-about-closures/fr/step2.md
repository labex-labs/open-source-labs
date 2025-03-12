# Les fermetures (Closures) en tant que générateur de code

Dans cette étape, nous allons apprendre comment les fermetures peuvent être utilisées pour générer du code de manière dynamique. Plus précisément, nous allons construire un système de vérification de type (type-checking) pour les attributs de classe en utilisant les fermetures.

Tout d'abord, comprenons ce qu'est une fermeture. Une fermeture est un objet fonction qui se souvient des valeurs de la portée englobante même si elles ne sont plus présentes en mémoire. En Python, les fermetures sont créées lorsqu'une fonction imbriquée fait référence à une valeur de sa fonction englobante.

Maintenant, commençons à implémenter notre système de vérification de type.

1. Créez un nouveau fichier nommé `typedproperty.py` dans le répertoire `/home/labex/project` avec le code suivant :

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Dans ce code, la fonction `typedproperty` est une fermeture. Elle prend deux arguments : `name` et `expected_type`. Le décorateur `@property` est utilisé pour créer une méthode getter pour la propriété, qui récupère la valeur de l'attribut privé. Le décorateur `@value.setter` crée une méthode setter qui vérifie si la valeur à définir est du type attendu. Sinon, elle lève une erreur `TypeError`.

2. Maintenant, créons une classe qui utilise ces propriétés typées. Créez un fichier nommé `stock.py` avec le code suivant :

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Dans la classe `Stock`, nous utilisons la fonction `typedproperty` pour créer des attributs avec vérification de type pour `name`, `shares` et `price`. Lorsque nous créons une instance de la classe `Stock`, la vérification de type sera appliquée automatiquement.

3. Créons un fichier de test pour voir cela en action. Créez un fichier nommé `test_stock.py` avec le code suivant :

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Dans ce fichier de test, nous créons d'abord un objet `Stock` avec les types corrects. Ensuite, nous essayons de définir l'attribut `shares` avec une chaîne de caractères, ce qui devrait lever une erreur `TypeError` car le type attendu est un entier.

4. Exécutez le fichier de test :

```bash
python3 test_stock.py
```

Vous devriez voir une sortie similaire à :

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

Cette sortie montre que la vérification de type fonctionne correctement.

5. Maintenant, améliorons le fichier `typedproperty.py` en ajoutant des fonctions pratiques pour les types courants. Ajoutez le code suivant à la fin du fichier :

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

Ces fonctions sont simplement des enveloppes autour de la fonction `typedproperty`, ce qui facilite la création de propriétés pour les types courants.

6. Créez un nouveau fichier nommé `stock_enhanced.py` qui utilise ces fonctions pratiques :

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Cette classe `Stock` utilise les fonctions pratiques pour créer des attributs avec vérification de type, ce qui rend le code plus lisible.

7. Créez un fichier de test `test_stock_enhanced.py` pour tester la version améliorée :

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Ce fichier de test est similaire au précédent, mais il teste la classe `Stock` améliorée.

8. Exécutez le test :

```bash
python3 test_stock_enhanced.py
```

Vous devriez voir une sortie similaire à :

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

Dans cette étape, nous avons démontré comment les fermetures peuvent être utilisées pour générer du code. La fonction `typedproperty` crée des objets propriétés qui effectuent une vérification de type, et les fonctions `String`, `Integer` et `Float` créent des propriétés spécialisées pour les types courants.
