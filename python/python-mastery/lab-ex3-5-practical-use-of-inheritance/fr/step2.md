# Définition d'une classe de formattage générique

Ajoutez la définition de classe suivante au fichier `tableformat.py` :

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

Maintenant, modifiez la fonction `print_table()` de sorte qu'elle accepte une instance de `TableFormatter` et invoque ses méthodes pour produire la sortie :

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Ces deux classes sont destinées à être utilisées ensemble. Par exemple :

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.TableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares', 'price'], formatter)
Traceback (most recent call last):
...
NotImplementedError
>>>
```

Pour l'instant, elle ne fait pas grand-chose d'intéressant. Vous allez corriger cela dans la section suivante.
