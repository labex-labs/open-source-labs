# Реализация конкретного форматировщика

`TableFormatter` не предназначен для самостоятельного использования. Вместо этого он лишь база для других классов, которые будут реализовывать форматирование. Добавьте следующий класс в `tableformat.py`:

```python
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 +'')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

Теперь используйте ваш новый класс следующим образом:

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
