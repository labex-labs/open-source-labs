# Implementando un formateador concret

La clase `TableFormatter` no está destinada a ser usada por sí sola. En cambio, es simplemente una base para otras clases que implementarán el formateo. Agrega la siguiente clase a `tableformat.py`:

```python
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 +'')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Ahora, usa tu nueva clase de la siguiente manera:

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
