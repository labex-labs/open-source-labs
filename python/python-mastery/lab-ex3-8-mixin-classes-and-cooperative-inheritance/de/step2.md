# Quer durch die Seiten

In der Datei `tableformat.py` fügen Sie die folgende Klassendefinition hinzu:

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Diese Klasse enthält eine einzelne Methode `row()`, die die Formatierung auf den Zeileninhalten anwendet. Eine Klassenvariable `formats` wird verwendet, um die Formatcodes zu speichern. Diese Klasse wird über Mehrfachvererbung verwendet. Beispielsweise:

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

Dieser gesamte Ansatz funktioniert, weil die Klasse `ColumnFormatMixin` zusammen mit einer anderen Klasse gemischt werden soll, die die erforderliche Methode `row()` bereitstellt.

Erstellen Sie eine andere Klasse, die einen Formatter dazu bringt, die Tabellenüberschriften in Großbuchstaben auszugeben:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Testen Sie es und bemerken Sie, dass die Überschriften jetzt in Großbuchstaben sind:

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

Das ist wirklich die ganze Idee hinter "Mixins". Der Schöpfer einer Bibliothek kann eine grundlegende Menge von Klassen wie `TextTableFormatter`, `CSVTableFormatter` usw. anbieten, um zu beginnen. Anschließend kann eine Sammlung von Ergänzungsklassen bereitgestellt werden, um diese Klassen auf verschiedene Weise verhalten zu lassen.
