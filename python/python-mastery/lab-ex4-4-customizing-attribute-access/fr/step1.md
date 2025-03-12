# Comprendre `__setattr__` pour le contrôle des attributs

En Python, il existe des méthodes spéciales qui vous permettent de personnaliser la manière dont les attributs d'un objet sont accédés et modifiés. Une méthode importante de ce type est `__setattr__()`. Cette méthode est appelée chaque fois que vous essayez d'assigner une valeur à un attribut d'un objet. Elle vous permet d'avoir un contrôle précis sur le processus d'assignation des attributs.

## Qu'est-ce que `__setattr__`?

La méthode `__setattr__(self, name, value)` agit comme un intercepteur pour toutes les assignations d'attributs. Lorsque vous écrivez une simple instruction d'assignation comme `obj.attr = value`, Python ne fait pas simplement une assignation directe de la valeur. Au lieu de cela, il appelle en interne `obj.__setattr__("attr", value)`. Ce mécanisme vous donne le pouvoir de décider ce qui devrait se passer lors de l'assignation de l'attribut.

Voyons maintenant un exemple pratique de l'utilisation de `__setattr__` pour restreindre quels attributs peuvent être définis sur une classe.

### Étape 1 : Créer un nouveau fichier

Tout d'abord, ouvrez un nouveau fichier dans l'IDE Web. Vous pouvez le faire en cliquant sur le menu "File" puis en sélectionnant "New File". Nommez ce fichier `restricted_stock.py` et enregistrez - le dans le répertoire `/home/labex/project`. Ce fichier contiendra la définition de la classe où nous utiliserons `__setattr__` pour contrôler l'assignation des attributs.

### Étape 2 : Ajouter du code à `restricted_stock.py`

Ajoutez le code suivant au fichier `restricted_stock.py`. Ce code définit une classe `RestrictedStock`.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

Dans la méthode `__init__`, nous initialisons l'objet avec les attributs `name`, `shares` et `price`. La méthode `__setattr__` vérifie si le nom de l'attribut en cours d'assignation se trouve dans l'ensemble des attributs autorisés (`name`, `shares`, `price`). Si ce n'est pas le cas, elle lève une `AttributeError`. Si l'attribut est autorisé, elle utilise la méthode `__setattr__` de la classe parente pour définir effectivement l'attribut.

### Étape 3 : Créer un fichier de test

Créez un nouveau fichier appelé `test_restricted.py` et ajoutez le code suivant. Ce code testera la fonctionnalité de la classe `RestrictedStock`.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

Dans ce code, nous importons d'abord la classe `RestrictedStock`. Ensuite, nous créons une instance de la classe. Nous testons l'accès aux attributs existants, la modification d'un attribut existant et, enfin, nous essayons de définir un attribut invalide pour voir si la méthode `__setattr__` fonctionne comme prévu.

### Étape 4 : Exécuter le fichier de test

Ouvrez un terminal dans l'IDE Web et exécutez les commandes suivantes pour exécuter le fichier `test_restricted.py` :

```bash
cd /home/labex/project
python3 test_restricted.py
```

Après avoir exécuté ces commandes, vous devriez voir une sortie similaire à celle - ci :

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## Comment cela fonctionne

La méthode `__setattr__` dans notre classe `RestrictedStock` fonctionne selon les étapes suivantes :

1. Elle vérifie d'abord si le nom de l'attribut se trouve dans l'ensemble autorisé (`name`, `shares`, `price`).
2. Si le nom de l'attribut n'est pas dans l'ensemble autorisé, elle lève une `AttributeError`. Cela empêche l'assignation d'attributs indésirables.
3. Si l'attribut est autorisé, elle utilise `super().__setattr__()` pour définir effectivement l'attribut. Cela garantit que le processus normal d'assignation d'attributs a lieu pour les attributs autorisés.

Cette méthode est plus flexible que l'utilisation de `__slots__`, que nous avons vu dans des exemples précédents. Bien que `__slots__` puisse optimiser l'utilisation de la mémoire et restreindre les attributs, il a des limitations lorsqu'il s'agit de l'héritage et peut entrer en conflit avec d'autres fonctionnalités de Python. Notre approche avec `__setattr__` nous donne un contrôle similaire sur l'assignation des attributs sans certaines de ces limitations.
