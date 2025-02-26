# Определение обобщенного класса форматировщика

Добавьте следующее определение класса в файл `tableformat.py`:

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

Теперь измените функцию `print_table()`, чтобы она принимала экземпляр `TableFormatter` и вызывала методы на нём для генерации вывода:

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Эти два класса предназначены для совместного использования. Например:

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

На данный момент это не делает ничего интересного. Вы почините это в следующем разделе.
