# Création d'une API conviviale pour les mixins

Les mixins sont une fonctionnalité puissante en Python, mais elles peuvent être un peu délicates pour les débutants car elles impliquent l'héritage multiple, qui peut devenir assez complexe. Dans cette étape, nous allons faciliter les choses pour les utilisateurs en améliorant la fonction `create_formatter()`. De cette façon, les utilisateurs n'auront pas à se soucier trop des détails de l'héritage multiple.

Tout d'abord, vous devez ouvrir le fichier `tableformat.py`. Vous pouvez le faire en exécutant les commandes suivantes dans votre terminal. La commande `cd` change le répertoire pour le dossier de votre projet, et la commande `code` ouvre le fichier `tableformat.py` dans votre éditeur de code.

```bash
cd ~/project
code tableformat.py
```

Une fois le fichier ouvert, recherchez la fonction `create_formatter()`. Actuellement, elle ressemble à ceci :

```python
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Cette fonction prend un nom en argument et renvoie le formateur correspondant. Mais nous voulons la rendre plus flexible. Nous allons la modifier pour qu'elle puisse accepter des arguments optionnels pour nos mixins.

Remplacez la fonction `create_formatter()` existante par la version améliorée ci-dessous. Cette nouvelle fonction vous permet de spécifier les formats de colonne et si les en-têtes doivent être convertis en majuscules.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

Cette fonction améliorée fonctionne en déterminant d'abord la classe de formateur de base en fonction de l'argument `name`. Ensuite, selon que `column_formats` et `upper_headers` sont fournis, elle crée une classe de formateur personnalisée qui inclut les mixins appropriés. Enfin, elle renvoie une instance de la classe de formateur personnalisée.

Maintenant, testons notre fonction améliorée avec différentes combinaisons d'options.

Tout d'abord, essayons d'utiliser le formatage des colonnes. Exécutez la commande suivante dans votre terminal. Cette commande importe les fonctions et les données nécessaires du fichier `tableformat.py`, crée un formateur avec le formatage des colonnes, puis affiche un tableau en utilisant ce formateur.

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Vous devriez voir le tableau avec des colonnes formatées. La sortie ressemblera à ceci :

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Ensuite, essayons d'utiliser des en-têtes en majuscules. Exécutez la commande suivante :

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Vous devriez voir le tableau avec des en-têtes en majuscules. La sortie sera :

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Enfin, combinons les deux options. Exécutez cette commande :

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Cela devrait afficher un tableau avec des colonnes formatées et des en-têtes en majuscules. La sortie sera :

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

La fonction améliorée fonctionne également avec d'autres types de formateurs. Par exemple, essayons-la avec le formateur CSV. Exécutez la commande suivante :

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Cela devrait produire une sortie CSV avec des colonnes formatées. La sortie sera :

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

En améliorant la fonction `create_formatter()`, nous avons créé une API conviviale. Les utilisateurs peuvent maintenant facilement utiliser les mixins sans avoir à comprendre les détails complexes de l'héritage multiple. Cela leur donne la flexibilité de personnaliser les formateurs selon leurs besoins.
