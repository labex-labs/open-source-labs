# Utilisation de `getattr()` pour le traitement générique d'objets

La fonction `getattr()` est un outil puissant en Python qui vous permet d'accéder aux attributs d'un objet de manière dynamique. Cela est particulièrement utile lorsque vous souhaitez traiter des objets de manière générique. Au lieu d'écrire un code spécifique à un type d'objet particulier, vous pouvez utiliser `getattr()` pour travailler avec n'importe quel objet qui possède les attributs requis. Cette flexibilité rend votre code plus réutilisable et adaptable.

## Traitement de plusieurs attributs

Commençons par apprendre à accéder à plusieurs attributs d'un objet à l'aide de la fonction `getattr()`. C'est un scénario courant lorsque vous avez besoin d'extraire des informations spécifiques d'un objet.

Tout d'abord, ouvrez l'interpréteur interactif Python si vous l'avez fermé précédemment. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```python
# Open a Python interactive shell if you closed the previous one
python3
```

Ensuite, nous allons importer la classe `Stock` et créer un objet `Stock`. La classe `Stock` représente une action avec des attributs tels que `name`, `shares` et `price`.

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

Maintenant, nous allons définir une liste de noms d'attributs auxquels nous souhaitons accéder. Cette liste nous aidera à itérer sur les attributs et à afficher leurs valeurs.

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

Enfin, nous allons utiliser une boucle `for` pour itérer sur la liste de noms d'attributs et accéder à chaque attribut à l'aide de `getattr()`. Nous afficherons le nom de l'attribut et sa valeur à chaque itération.

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

Lorsque vous exécutez ce code, vous verrez la sortie suivante :

```
name: GOOG
shares: 100
price: 490.1
```

Cette sortie montre que nous avons pu accéder et afficher les valeurs de plusieurs attributs de l'objet `Stock` à l'aide de la fonction `getattr()`.

## Valeurs par défaut avec `getattr()`

La fonction `getattr()` offre également une fonctionnalité utile : la possibilité de spécifier une valeur par défaut si l'attribut auquel vous essayez d'accéder n'existe pas. Cela peut empêcher votre code de lever une erreur `AttributeError` et le rendre plus robuste.

Voyons comment cela fonctionne. Tout d'abord, nous allons essayer d'accéder à un attribut qui n'existe pas dans l'objet `Stock`. Nous utiliserons `getattr()` et fournirons une valeur par défaut de `'N/A'`.

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

Dans ce cas, puisque l'attribut `symbol` n'existe pas dans l'objet `Stock`, `getattr()` retourne la valeur par défaut `'N/A'`.

Maintenant, comparons cela avec l'accès à un attribut existant. Nous allons accéder à l'attribut `name`, qui existe dans l'objet `Stock`.

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

Ici, `getattr()` retourne la valeur réelle de l'attribut `name`, qui est `'GOOG'`.

## Traitement d'une collection d'objets

La fonction `getattr()` devient encore plus puissante lorsque vous avez besoin de traiter une collection d'objets. Voyons comment nous pouvons l'utiliser pour traiter un portefeuille d'actions.

Tout d'abord, nous allons importer la fonction `read_portfolio` du module `stock`. Cette fonction lit un portefeuille d'actions à partir d'un fichier CSV et retourne une liste d'objets `Stock`.

```python
# Import the portfolio reading function
from stock import read_portfolio
```

Ensuite, nous allons utiliser la fonction `read_portfolio` pour lire le portefeuille à partir d'un fichier CSV nommé `portfolio.csv`.

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

Enfin, nous allons utiliser une boucle `for` pour itérer sur la liste d'objets `Stock` dans le portefeuille. Pour chaque action, nous utiliserons `getattr()` pour accéder aux attributs `name` et `shares` et afficher leurs valeurs.

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

Cette approche rend votre code plus flexible car vous pouvez travailler avec les noms d'attributs sous forme de chaînes de caractères. Ces chaînes peuvent être passées en tant qu'arguments ou stockées dans des structures de données, vous permettant de changer facilement les attributs auxquels vous souhaitez accéder sans modifier la logique principale de votre code.
