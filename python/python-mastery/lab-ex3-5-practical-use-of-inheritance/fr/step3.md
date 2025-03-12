# Implémentation d'un formateur concret

Maintenant que nous avons défini notre classe abstraite de base et mis à jour la fonction `print_table()`, il est temps de créer une classe de formateur concret. Une classe de formateur concret est une classe qui fournit des implémentations réelles pour les méthodes définies dans la classe abstraite de base. Dans notre cas, nous allons créer une classe qui peut formater les données en un tableau texte brut.

Ajoutons la classe suivante à votre fichier `tableformat.py`. Cette classe héritera de la classe abstraite de base `TableFormatter` et implémentera les méthodes `headings()` et `row()`.

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

La classe `TextTableFormatter` hérite de `TableFormatter`. Cela signifie qu'elle obtient toutes les propriétés et méthodes de la classe `TableFormatter`, mais elle fournit également ses propres implémentations pour les méthodes `headings()` et `row()`. Ces méthodes sont respectivement responsables du formatage des en - têtes et des lignes du tableau. La méthode `headings()` affiche les en - têtes d'une manière bien formatée, suivie d'une ligne de tirets pour séparer les en - têtes des données. La méthode `row()` formate chaque ligne de données de manière similaire.

Maintenant, testons notre nouveau formateur. Nous allons utiliser les modules `stock`, `reader` et `tableformat` pour lire les données à partir d'un fichier CSV et les afficher en utilisant notre nouveau formateur.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Lorsque vous exécutez ce code, vous devriez voir la même sortie que précédemment. C'est parce que notre nouveau formateur est conçu pour produire le même tableau texte brut que la fonction `print_table()` originale.

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

Cette sortie confirme que notre `TextTableFormatter` fonctionne correctement. L'avantage d'utiliser cette approche est que nous avons rendu notre code plus modulaire et extensible. En séparant la logique de formatage dans une hiérarchie de classes distincte, nous pouvons facilement ajouter de nouveaux formats de sortie. Tout ce que nous avons à faire est de créer de nouvelles sous - classes de `TableFormatter` sans modifier la fonction `print_table()`. De cette façon, nous pourrons prendre en charge différents formats de sortie tels que CSV ou HTML à l'avenir.
