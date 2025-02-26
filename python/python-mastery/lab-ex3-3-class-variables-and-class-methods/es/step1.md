# Laboratorio anterior

Las instancias de la clase `Stock` definida en el laboratorio anterior se crean normalmente de la siguiente manera:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

Sin embargo, la función `read_portfolio()` también crea instancias a partir de filas de datos leídas de archivos. Por ejemplo, se utiliza código como el siguiente:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
