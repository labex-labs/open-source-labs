# Implémentation d'un formateur concret

La classe `TableFormatter` n'est pas destinée à être utilisée seule. Au contraire, elle est simplement une base pour d'autres classes qui implémenteront le formattage. Ajoutez la classe suivante à `tableformat.py` :

```python
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 +'')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Maintenant, utilisez votre nouvelle classe comme suit :

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.TextTableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares', 'price'], formatter)
     name     shares      price
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
