# Definition einer generischen Formatter-Klasse

Fügen Sie die folgende Klassendefinition zur Datei `tableformat.py` hinzu:

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

Ändern Sie nun die Funktion `print_table()`, sodass sie eine `TableFormatter`-Instanz akzeptiert und auf ihr Methoden aufruft, um die Ausgabe zu erzeugen:

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Diese beiden Klassen sind zusammenzusetzen. Beispielsweise:

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

Im Moment macht es noch nicht viel Interessantes. Dies werden Sie im nächsten Abschnitt beheben.
