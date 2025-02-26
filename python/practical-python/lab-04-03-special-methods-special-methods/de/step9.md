# Übung 4.10: Ein Beispiel für die Verwendung von getattr()

`getattr()` ist ein alternatives Mechanismus zum Lesen von Attributen. Es kann verwendet werden, um extrem flexiblen Code zu schreiben. Beginnen Sie mit diesem Beispiel:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name','shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

Beobachten Sie genau, dass die Ausgabedaten vollständig durch die in der `columns`-Variable aufgelisteten Attributnamen bestimmt werden.

In der Datei `tableformat.py` nehmen Sie diese Idee und erweitern Sie sie zu einer verallgemeinerten Funktion `print_table()`, die eine Tabelle druckt, die benutzerdefinierte Attribute einer Liste beliebiger Objekte zeigt. Wie bei der früheren `print_report()`-Funktion sollte `print_table()` auch eine `TableFormatter`-Instanz akzeptieren, um das Ausgabeformat zu steuern. So sollte es funktionieren:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares', 'price'], formatter)
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
