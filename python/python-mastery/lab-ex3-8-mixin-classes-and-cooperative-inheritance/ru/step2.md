# Переход вбок

В файле `tableformat.py` добавьте следующее определение класса:

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

В этом классе содержится единственный метод `row()`, который применяет форматирование к содержимому строки. Переменная класса `formats` используется для хранения кодов форматирования. Этот класс используется с помощью множественного наследования. Например:

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

Вся эта схема работает, потому что класс `ColumnFormatMixin` предназначен для объединения с другим классом, который предоставляет необходимый метод `row()`.

Создайте другой класс, который заставляет форматтер выводить заголовки таблицы заглавными буквами:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

Попробуйте его и заметьте, что заголовки теперь записаны заглавными буквами:

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

Это действительно вся идея "миксинов". Создатель библиотеки может предоставить базовый набор классов, таких как `TextTableFormatter`, `CSVTableFormatter` и т.д., чтобы начать. Затем можно предоставить коллекцию дополнительных классов, чтобы заставить эти классы вести себя по-разному.
