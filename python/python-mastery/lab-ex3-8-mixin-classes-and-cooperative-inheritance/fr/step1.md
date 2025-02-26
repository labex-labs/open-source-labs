# Le problème de la mise en forme des colonnes

Si vous revenez au TP 3.1, vous avez écrit une fonction `print_portfolio()` qui produisait un tableau comme celui-ci :

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

La fonction `print_table()` développée dans les derniers exercices remplace presque cette fonctionnalité - presque. Le seul problème qu'elle a est qu'elle ne peut pas formater précisément le contenu de chaque colonne. Par exemple, remarquez comment les valeurs de la colonne `price` sont formatées précisément avec 2 décimales. La classe `TableFormatter` et les sous-classes connexes ne peuvent pas faire cela.

Une manière de le corriger serait de modifier la fonction `print_table()` pour accepter un argument supplémentaire `formats`. Par exemple, peut-être quelque chose comme ceci :

```python
>>> def print_table(records, fields, formats, formatter):
        formatter.headings(fields)
        for r in records:
            rowdata = [(fmt % getattr(r, fieldname))
                 for fieldname,fmt in zip(fields,formats)]
            formatter.row(rowdata)

>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> from tableformat import TextTableFormatter
>>> formatter = TextTableFormatter()
>>> print_table(portfolio,
                ['name','shares','price'],
                ['%s','%d','%0.2f'],
                formatter)

      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Oui, vous pourriez modifier `print_table()` ainsi, mais est-ce le bon endroit pour le faire? L'idée générale de toutes les classes `TableFormatter` est qu'elles peuvent être utilisées dans différents types d'applications. La mise en forme des colonnes est quelque chose qui pourrait être utile ailleurs, pas seulement dans la fonction `print_table()`.

Une autre approche possible serait de modifier l'interface de la classe `TableFormatter` d'une certaine manière. Par exemple, peut-être en ajoutant une troisième méthode pour appliquer la mise en forme.

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

Le problème ici est que chaque fois que vous modifiez l'interface d'une classe, vous devrez refactoriser tout le code existant pour qu'il fonctionne avec elle. Plus précisément, vous devrez modifier toutes les sous-classes `TableFormatter` déjà écrites et tout le code écrit pour les utiliser. Ne faisons pas ça.

En alternative, un utilisateur pourrait utiliser l'héritage pour personnaliser un formatteur spécifique afin d'y injecter une certaine mise en forme. Par exemple, essayez cet exemple :

```python
>>> from tableformat import TextTableFormatter, print_table
>>> class PortfolioFormatter(TextTableFormatter):
        def row(self, rowdata):
            formats = ['%s','%d','%0.2f']
            rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
            super().row(rowdata)

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
>>>
```

Oui, cela fonctionne, mais c'est également un peu maladroit et étrange. L'utilisateur doit choisir un formatteur spécifique à personnaliser. De plus, ils doivent implémenter le code de mise en forme des colonnes réel eux-mêmes. Assurément, il existe une autre manière de faire cela.
