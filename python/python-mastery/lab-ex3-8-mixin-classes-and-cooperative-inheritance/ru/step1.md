# Проблема с форматированием столбцов

Если вы вспомните упражнение 3.1, вы написали функцию `print_portfolio()`, которая выводила таблицу такого вида:

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

Функция `print_table()`, разработанная в нескольких последних упражнениях, почти заменяет эту функциональность - почти. Одна проблема, с которой она столкнулась, заключается в том, что она не может точно отформатировать содержимое каждого столбца. Например, обратите внимание, как значения в столбце `price` точно отформатированы с двумя десятичными знаками. Класс `TableFormatter` и связанные подклассы не могут этого сделать.

Одним из способов исправить это было бы модифицировать функцию `print_table()` так, чтобы она принимала дополнительный аргумент `formats`. Например, может быть что-то вроде этого:

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

Да, вы могли бы модифицировать `print_table()` так, но это правильное место для этого? Вся идея всех классов `TableFormatter` заключается в том, что они могут использоваться в различных приложениях. Форматирование столбцов может быть полезным в других местах, не только в функции `print_table()`.

Другой возможный подход - изменить интерфейс класса `TableFormatter` каким-то образом. Например, может быть добавлен третий метод для применения форматирования.

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

Проблема здесь заключается в том, что каждый раз, когда вы изменяете интерфейс класса, вы должны переписать весь существующий код, чтобы он работал с ним. В частности, вам нужно будет изменить все уже написанные подклассы `TableFormatter` и весь код, написанный для их использования. Давайте этого не будем делать.

Вместо этого пользователь может использовать наследование для настройки конкретного форматтера, чтобы внедрить в него некоторое форматирование. Например, попробуйте этот эксперимент:

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

Да, это работает, но это также немного неуклюже и странно. Пользователю нужно выбрать конкретный форматтер для настройки. Кроме того, они должны сами реализовать фактический код форматирования столбцов. Конечно, существует другой способ сделать это.
