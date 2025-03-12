# Ajout de la vérification de types à print_table()

Dans cette étape, nous allons améliorer la fonction `print_table()` dans le fichier `tableformat.py`. Nous allons ajouter une vérification pour voir si le paramètre `formatter` est une instance valide de `TableFormatter`. Pourquoi avons - nous besoin de cela ? Eh bien, la vérification de types est comme un filet de sécurité pour votre code. Elle permet de s'assurer que les données avec lesquelles vous travaillez sont du bon type, ce qui peut éviter de nombreux bugs difficiles à trouver.

## Comprendre la vérification de types en Python

La vérification de types est une technique très utile en programmation. Elle vous permet de détecter les erreurs dès le début du processus de développement. En Python, nous avons souvent à faire avec différents types d'objets, et parfois nous attendons qu'un certain type d'objet soit passé à une fonction. Pour vérifier si un objet est d'un type spécifique ou d'une sous - classe de ce type, nous pouvons utiliser la fonction `isinstance()`. Par exemple, si vous avez une fonction qui attend une liste, vous pouvez utiliser `isinstance()` pour vous assurer que l'entrée est bien une liste.

## Modification de la fonction print_table()

Tout d'abord, ouvrez le fichier `tableformat.py` dans votre éditeur de code. Faites défiler jusqu'au bas du fichier, et vous trouverez la fonction `print_table()`. Voici à quoi elle ressemble initialement :

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

Cette fonction prend des données, une liste de colonnes et un formateur. Elle utilise ensuite le formateur pour afficher un tableau. Mais pour l'instant, elle ne vérifie pas si le formateur est du bon type.

Modifions - la pour ajouter la vérification de type. Nous allons utiliser la fonction `isinstance()` pour vérifier si le paramètre `formatter` est une instance de `TableFormatter`. Si ce n'est pas le cas, nous leverons une `TypeError` avec un message clair. Voici le code modifié :

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Test de votre implémentation de la vérification de types

Maintenant que nous avons ajouté la vérification de type, nous devons nous assurer qu'elle fonctionne. Créons un nouveau fichier Python appelé `test_tableformat.py`. Voici le code que vous devriez y mettre :

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

Dans ce code, nous lisons d'abord des données de portefeuille. Ensuite, nous définissons une nouvelle classe de formateur appelée `MyFormatter` qui n'hérite pas de `TableFormatter`. Nous essayons d'utiliser ce formateur non conforme dans la fonction `print_table()`. Si notre vérification de type fonctionne, elle devrait lever une `TypeError`.

Pour exécuter le test, ouvrez votre terminal et naviguez jusqu'au répertoire où se trouve le fichier `test_tableformat.py`. Ensuite, exécutez la commande suivante :

```bash
python test_tableformat.py
```

Si tout fonctionne correctement, vous devriez voir une sortie comme celle - ci :

```
Test passed - caught error: Expected a TableFormatter
```

Cette sortie confirme que notre vérification de type fonctionne comme prévu. Maintenant, la fonction `print_table()` n'acceptera que des formateurs qui sont des instances de `TableFormatter` ou de l'une de ses sous - classes.
