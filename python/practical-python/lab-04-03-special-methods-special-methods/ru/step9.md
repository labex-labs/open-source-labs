# Упражнение 4.10: Пример использования getattr()

`getattr()` - это альтернативный механизм для чтения атрибутов. Его можно использовать для написания чрезвычайно гибкого кода. Сначала попробуйте этот пример:

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

Обратите внимание, что выходные данные определяются полностью именами атрибутов, перечисленными в переменной `columns`.

В файле `tableformat.py` развяжите эту идею и расширьте ее до обобщенной функции `print_table()`, которая выводит таблицу с указанными пользователем атрибутами списка произвольных объектов. Как и раньше функция `print_report()`, `print_table()` должна также принимать экземпляр `TableFormatter` для управления форматом вывода. Вот, как это должно работать:

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
