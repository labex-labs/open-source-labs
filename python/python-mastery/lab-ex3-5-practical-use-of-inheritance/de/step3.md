# Implementierung eines konkreten Formatters

Die `TableFormatter` ist nicht für die alleinige Verwendung gedacht. Stattdessen ist sie lediglich eine Grundlage für andere Klassen, die die Formatierung implementieren werden. Fügen Sie die folgende Klasse zu `tableformat.py` hinzu:

```python
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 +'')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Verwenden Sie nun Ihre neue Klasse wie folgt:

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
