# Definiendo una clase formateadora genérica

Agrega la siguiente definición de clase al archivo `tableformat.py`:

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

Ahora, modifica la función `print_table()` de modo que acepte una instancia de `TableFormatter` e invoque métodos en ella para producir la salida:

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

Estas dos clases están destinadas a ser usadas juntas. Por ejemplo:

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

Por ahora, no hace nada muy interesante. Lo arreglarás en la siguiente sección.
