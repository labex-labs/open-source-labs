# Comprendre l'accès aux attributs en Python

En Python, les objets sont un concept fondamental. Ils peuvent stocker des données dans des attributs, qui sont comme des conteneurs nommés pour les valeurs. Vous pouvez considérer les attributs comme des variables appartenant à un objet. Il existe plusieurs façons d'accéder à ces attributs. La méthode la plus simple et la plus couramment utilisée est la notation pointée (`.`). Cependant, Python propose également des fonctions spécifiques qui vous offrent plus de flexibilité lors de la manipulation des attributs.

## La notation pointée

Commençons par créer un objet `Stock` et voyons comment nous pouvons manipuler ses attributs à l'aide de la notation pointée. La notation pointée est un moyen simple et intuitif d'accéder et de modifier les attributs d'un objet.

Tout d'abord, ouvrez un nouveau terminal et lancez l'interpréteur interactif Python. C'est là que vous pouvez écrire et exécuter du code Python ligne par ligne.

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

Dans le code ci - dessus, nous importons d'abord la classe `Stock` du module `stock`. Ensuite, nous créons une instance de la classe `Stock` nommée `s`. Pour obtenir la valeur de l'attribut `name`, nous utilisons `s.name`. Pour modifier la valeur de l'attribut `shares`, nous assignons simplement une nouvelle valeur à `s.shares`. Et si nous voulons supprimer un attribut, nous utilisons le mot - clé `del` suivi du nom de l'attribut.

## Fonctions d'accès aux attributs

Python fournit quatre fonctions intégrées très utiles pour la manipulation des attributs. Ces fonctions vous donnent plus de contrôle lors de la manipulation des attributs, en particulier lorsque vous devez les gérer de manière dynamique.

1. `getattr()` - Cette fonction est utilisée pour obtenir la valeur d'un attribut.
2. `setattr()` - Elle vous permet de définir la valeur d'un attribut.
3. `delattr()` - Vous pouvez utiliser cette fonction pour supprimer un attribut.
4. `hasattr()` - Cette fonction vérifie si un attribut existe dans un objet.

Voyons comment utiliser ces fonctions :

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

Ces fonctions sont particulièrement utiles lorsque vous devez travailler avec des attributs de manière dynamique. Au lieu d'utiliser des noms d'attributs codés en dur, vous pouvez utiliser des noms de variables. Par exemple, si vous avez une variable qui stocke le nom d'un attribut, vous pouvez passer cette variable à ces fonctions pour effectuer des opérations sur l'attribut correspondant. Cela vous offre plus de flexibilité dans votre code, en particulier lorsque vous travaillez avec différents objets et attributs de manière plus dynamique.
