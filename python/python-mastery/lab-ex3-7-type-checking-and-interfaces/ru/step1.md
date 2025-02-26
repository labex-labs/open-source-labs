# Интерфейсы и проверка типов

Измените функцию `print_table()`, чтобы она проверяла, наследуется ли переданный экземпляр форматтера от `TableFormatter`. Если нет, вызывайте `TypeError`.

Ваш новый код должен ловить такие ситуации:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

Добавление такой проверки может добавить некоторую степень безопасности в программу. Однако вы должны помнить, что проверка типов в Python довольно слабая. Нет гарантии, что объект, переданный в качестве форматтера, будет работать правильно, даже если он碰巧 наследуется от соответствующего базового класса. Следующая часть посвящена этому вопросу.
