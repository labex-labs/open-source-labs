# Défi : Utilisation d'un objet appelable comme méthode

En Python, lorsque vous utilisez un objet appelable (callable object) comme méthode au sein d'une classe, vous devez relever un défi unique. Un objet appelable est quelque chose que vous pouvez "appeler" comme une fonction, comme une fonction elle-même ou un objet avec une méthode `__call__`. Lorsqu'il est utilisé comme méthode de classe, cela ne fonctionne pas toujours comme prévu en raison de la façon dont Python passe l'instance (`self`) comme premier argument.

Explorons ce problème en créant une classe `Stock`. Cette classe représentera une action avec des attributs tels que le nom, le nombre de parts et le prix. Nous utiliserons également un validateur pour nous assurer que les données avec lesquelles nous travaillons sont correctes.

Tout d'abord, ouvrez le fichier `stock.py` pour commencer à écrire notre classe `Stock`. Vous pouvez utiliser la commande suivante pour ouvrir le fichier dans un éditeur :

```bash
code /home/labex/project/stock.py
```

Maintenant, ajoutez le code suivant au fichier `stock.py`. Ce code définit la classe `Stock` avec une méthode `__init__` pour initialiser les attributs de l'action, une propriété `cost` pour calculer le coût total et une méthode `sell` pour réduire le nombre de parts. Nous essaierons également d'utiliser la classe `ValidatedFunction` pour valider l'entrée de la méthode `sell`.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

Après avoir défini la classe `Stock`, nous devons la tester pour voir si elle fonctionne comme prévu. Créez un fichier de test nommé `test_stock.py` et ouvrez-le en utilisant la commande suivante :

```bash
code /home/labex/project/test_stock.py
```

Ajoutez le code suivant au fichier `test_stock.py`. Ce code crée une instance de la classe `Stock`, affiche le nombre initial de parts et le coût, essaie de vendre quelques parts, puis affiche le nombre de parts mis à jour et le coût.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Maintenant, exécutez le fichier de test en utilisant la commande suivante :

```bash
python3 /home/labex/project/test_stock.py
```

Vous rencontrerez probablement une erreur similaire à :

```
Error: missing a required argument: 'nshares'
```

Cette erreur se produit parce que lorsque Python appelle une méthode comme `s.sell(10)`, il appelle en réalité `Stock.sell(s, 10)` en arrière-plan. Le paramètre `self` représente l'instance de la classe, et il est automatiquement passé comme premier argument. Cependant, notre classe `ValidatedFunction` ne gère pas correctement ce paramètre `self` car elle ne sait pas qu'elle est utilisée comme méthode.

**Comprendre le problème**

Lorsque vous définissez une méthode à l'intérieur d'une classe puis la remplacez par une instance de `ValidatedFunction`, vous enveloppez essentiellement la méthode originale. Le problème est que la méthode enveloppée ne gère pas correctement le paramètre `self` automatiquement. Elle attend les arguments d'une manière qui ne prend pas en compte le fait que l'instance est passée comme premier argument.

**Résoudre le problème**

Pour résoudre ce problème, nous devons modifier la façon dont nous gérons les méthodes. Nous allons créer une nouvelle classe appelée `ValidatedMethod` qui peut gérer correctement les appels de méthode. Ajoutez le code suivant à la fin du fichier `validate.py` :

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Maintenant, nous devons modifier la classe `Stock` pour utiliser `ValidatedMethod` au lieu de `ValidatedFunction`. Ouvrez à nouveau le fichier `stock.py` :

```bash
code /home/labex/project/stock.py
```

Mettez à jour la classe `Stock` comme suit :

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

La classe `ValidatedMethod` est un descripteur (descriptor), qui est un type spécial d'objet en Python qui peut modifier la façon dont les attributs sont accédés. La méthode `__get__` est appelée lorsque l'attribut est accédé comme une méthode. Elle retourne un objet appelable qui passe correctement l'instance comme premier argument.

Exécutez à nouveau le fichier de test en utilisant la commande suivante :

```bash
python3 /home/labex/project/test_stock.py
```

Maintenant, vous devriez voir une sortie similaire à :

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

Ce défi vous a montré un aspect important des objets appelables. Lorsque vous les utilisez comme méthodes dans une classe, ils nécessitent un traitement spécial. En implémentant le protocole de descripteur avec la méthode `__get__`, nous pouvons créer des objets appelables qui fonctionnent correctement à la fois comme fonctions autonomes et comme méthodes.
