# Configurando algunos datos

Comience el ejercicio tomando algunas filas de datos de un archivo CSV.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> headers
['name','shares', 'price']
>>> rows = list(f_csv)
>>> from pprint import pprint
>>> pprint(rows)
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
>>>
```
