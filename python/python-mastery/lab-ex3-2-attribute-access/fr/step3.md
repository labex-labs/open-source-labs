# Création d'un formateur de table en utilisant l'accès aux attributs

En programmation, l'accès aux attributs est un concept fondamental qui nous permet d'interagir avec les propriétés des objets. Maintenant, nous allons mettre en pratique ce que nous avons appris sur l'accès aux attributs. Nous allons créer un utilitaire utile : un formateur de table. Ce formateur prendra une collection d'objets et les affichera sous forme de tableau, rendant les données plus faciles à lire et à comprendre.

## Création du module tableformat.py

Tout d'abord, nous devons créer un nouveau fichier Python. Ce fichier contiendra le code de notre formateur de table.

Pour créer le fichier, suivez ces étapes :

1. Dans l'IDE Web, cliquez sur le menu "File".
2. Dans le menu déroulant, sélectionnez "New File".
3. Enregistrez le fichier nouvellement créé sous le nom `tableformat.py` dans le répertoire `/home/labex/project/`.

Maintenant que nous avons notre fichier, écrivons le code de la fonction `print_table()` dans `tableformat.py`. Cette fonction sera chargée de formater et d'afficher nos objets sous forme de tableau.

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

Analysons ce que fait cette fonction :

1. Elle prend deux arguments : une séquence d'objets et une liste de noms d'attributs. La séquence d'objets est les données que nous voulons afficher, et la liste de noms d'attributs indique à la fonction quelles propriétés des objets afficher.
2. Elle affiche une ligne d'en-tête. La ligne d'en-tête contient les noms des attributs qui nous intéressent.
3. Elle affiche une ligne de séparation. Cette ligne aide à séparer visuellement l'en-tête des données.
4. Pour chaque objet de la séquence, elle affiche la valeur de chaque attribut spécifié. Elle utilise la fonction `getattr()` pour accéder à la valeur de l'attribut de chaque objet.

Maintenant, testons notre fonction `print_table()` pour voir si elle fonctionne comme prévu.

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Lorsque vous exécutez le code ci-dessus, vous devriez voir la sortie suivante :

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

L'un des grands avantages de notre fonction `print_table()` est sa flexibilité. Nous pouvons changer les colonnes affichées simplement en modifiant la liste `fields`.

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

L'exécution de ce code vous donnera la sortie suivante :

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

La force de cette approche réside dans sa généralité. Nous pouvons utiliser la même fonction `print_table()` pour afficher des tableaux pour n'importe quel type d'objet, tant que nous connaissons les noms des attributs que nous voulons afficher. Cela fait de notre formateur de table un outil très utile dans notre boîte à outils de programmation.
