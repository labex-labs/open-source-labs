# Das Problem mit der Spaltenformatierung

Wenn Sie alle den Weg zurück zu Übung 3.1 gehen, haben Sie eine Funktion `print_portfolio()` geschrieben, die eine Tabelle wie diese erzeugt hat:

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

Die in den letzten mehreren Übungen entwickelte Funktion `print_table()` ersetzt fast diese Funktionalität - fast. Das eine Problem, das sie hat, ist, dass sie den Inhalt jeder Spalte nicht präzise formatieren kann. Beispielsweise bemerken Sie, wie die Werte in der `price`-Spalte präzise mit 2 Dezimalstellen formatiert sind. Die `TableFormatter`-Klasse und die zugehörigen Unterklassen können das nicht.

Eine Möglichkeit, es zu beheben, wäre, die Funktion `print_table()` zu ändern, um ein zusätzliches `formats`-Argument zu akzeptieren. Beispielsweise könnte es so aussehen:

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

Ja, Sie könnten `print_table()` so ändern, aber ist das der richtige Ort dafür? Die ganze Idee aller `TableFormatter`-Klassen ist, dass sie in verschiedenen Arten von Anwendungen verwendet werden können. Die Spaltenformatierung ist etwas, das an anderen Stellen nützlich sein könnte, nicht nur in der `print_table()`-Funktion.

Ein anderer möglicher Ansatz könnte sein, die Schnittstelle der `TableFormatter`-Klasse auf某种方式zu ändern. Beispielsweise könnte man vielleicht eine dritte Methode hinzufügen, um die Formatierung anzuwenden.

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

Das Problem hier ist, dass jedes Mal, wenn Sie die Schnittstelle einer Klasse ändern, müssen Sie den gesamten vorhandenen Code umgestalten, um mit ihr zu arbeiten. Insbesondere müssten Sie alle bereits geschriebenen `TableFormatter`-Unterklassen und den gesamten Code ändern, der geschrieben wurde, um sie zu verwenden. Lassen Sie uns das nicht tun.

Als Alternative könnte ein Benutzer die Vererbung verwenden, um einen bestimmten Formatter anzupassen, um einige Formatierungen hineinzufügen. Beispielsweise versuchen Sie dieses Experiment:

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

Ja, das funktioniert, aber es ist auch ein bisschen umständlich und seltsam. Der Benutzer muss einen bestimmten Formatter auswählen, um ihn anzupassen. Darüber hinaus müssen sie den tatsächlichen Spaltenformatierungs-Code selbst implementieren. Sicherlich gibt es eine andere Möglichkeit, das zu tun.
