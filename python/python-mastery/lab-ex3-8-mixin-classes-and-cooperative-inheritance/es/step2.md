# Imitando a un cangrejo

En el archivo `tableformat.py`, agregue la siguiente definición de clase:

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

Esta clase contiene un único método `row()` que aplica un formato a los contenidos de la fila. Una variable de clase `formats` se utiliza para almacenar los códigos de formato. Esta clase se utiliza a través de la herencia múltiple. Por ejemplo:

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

Todo este enfoque funciona porque la clase `ColumnFormatMixin` está destinada a ser combinada con otra clase que proporcione el método `row()` requerido.

Cree otra clase que haga que un formateador imprima los encabezados de la tabla en mayúsculas:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Pruebe esto y observe que los encabezados ahora están en mayúsculas:

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

Esta es realmente la idea general de los "mixins". El creador de una biblioteca puede proporcionar un conjunto básico de clases como `TextTableFormatter`, `CSVTableFormatter`, etc., para comenzar. Luego, se puede proporcionar una colección de clases complementarias para hacer que esas clases se comporten de diferentes maneras.
