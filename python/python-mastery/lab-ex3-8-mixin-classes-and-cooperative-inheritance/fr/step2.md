# Aller de côté

Dans le fichier `tableformat.py`, ajoutez la définition de classe suivante :

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Cette classe contient une seule méthode `row()` qui applique une mise en forme au contenu de la ligne. Une variable de classe `formats` est utilisée pour stocker les codes de mise en forme. Cette classe est utilisée via l'héritage multiple. Par exemple :

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> from tableformat import TextTableFormatter, ColumnFormatMixin, print_table
>>> class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
        formats = ['%s', '%d', '%0.2f']

>>> formatter = PortfolioFormatter()
>>> print_table(portfolio, ['name','shares','price'], formatter)
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

Toute cette approche fonctionne car la classe `ColumnFormatMixin` est conçue pour être combinée avec une autre classe qui fournit la méthode `row()` requise.

Créez une autre classe qui fait en sorte qu'un formatteur affiche les en-têtes du tableau en majuscules :

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Essayez-le et remarquez que les en-têtes sont maintenant en majuscules :

```python
>>> from tableformat import TextTableFormatter, UpperHeadersMixin
>>> class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
        pass

>>> formatter = PortfolioFormatter()
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

C'est vraiment l'idée principale des "mixins". Le créateur d'une bibliothèque peut fournir un ensemble de classes de base telles que `TextTableFormatter`, `CSVTableFormatter`, etc. pour commencer. Ensuite, une collection de classes complémentaires peut être fournie pour que ces classes se comportent de différentes manières.
