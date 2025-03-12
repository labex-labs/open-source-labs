# Création d'une classe de base et modification de la fonction d'impression

En programmation, l'héritage est un concept puissant qui nous permet de créer une hiérarchie de classes. Pour commencer à utiliser l'héritage pour afficher des données dans différents formats, nous devons d'abord créer une classe de base. Une classe de base sert de modèle pour d'autres classes, en définissant un ensemble commun de méthodes que ses sous - classes peuvent hériter et redéfinir.

Maintenant, créons une classe de base qui définira l'interface pour tous les formateurs de tableaux. Ouvrez le fichier `tableformat.py` dans le WebIDE et ajoutez le code suivant en haut du fichier :

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

La classe `TableFormatter` est une classe abstraite de base. Une classe abstraite de base est une classe qui définit des méthodes mais ne fournit pas d'implémentations pour elles. Au lieu de cela, elle attend que ses sous - classes fournissent ces implémentations. Les exceptions `NotImplementedError` sont utilisées pour indiquer que ces méthodes doivent être redéfinies par les sous - classes. Si une sous - classe ne redéfinit pas ces méthodes et que nous essayons de les utiliser, une erreur sera levée.

Ensuite, nous devons modifier la fonction `print_table()` pour utiliser la classe `TableFormatter`. La fonction `print_table()` est utilisée pour afficher un tableau de données à partir d'une liste d'objets. En la modifiant pour utiliser la classe `TableFormatter`, nous pouvons rendre la fonction plus flexible et capable de fonctionner avec différents formats de tableaux.

Remplacez la fonction `print_table()` existante par le code suivant :

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Le changement clé ici est que `print_table()` prend maintenant un paramètre `formatter`, qui doit être une instance de `TableFormatter` ou d'une sous - classe. Cela signifie que nous pouvons passer différents formateurs de tableaux à la fonction `print_table()`, et elle utilisera le formateur approprié pour afficher le tableau. La fonction délègue la responsabilité de formatage à l'objet formateur en appelant ses méthodes `headings()` et `row()`.

Testons nos modifications en essayant d'utiliser la classe de base `TableFormatter` :

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Lorsque vous exécutez ce code, vous devriez voir une erreur :

```
Traceback (most recent call last):
...
NotImplementedError
```

Cette erreur se produit parce que nous essayons d'utiliser directement la classe abstraite de base, mais elle ne fournit pas d'implémentations pour ses méthodes. Étant donné que les méthodes `headings()` et `row()` dans la classe `TableFormatter` lèvent `NotImplementedError`, Python ne sait pas quoi faire lorsque ces méthodes sont appelées. Dans l'étape suivante, nous allons créer une sous - classe concrète qui fournit ces implémentations.
