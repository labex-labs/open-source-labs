# Ejercicio 2.23: Extracción de datos de archivos CSV

Saberse utilizar diversas combinaciones de comprensiones de lista, conjunto y diccionario puede ser útil en diversas formas de procesamiento de datos. Aquí hay un ejemplo que muestra cómo extraer columnas seleccionadas de un archivo CSV.

Primero, lee una fila de información de encabezado de un archivo CSV:

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

Luego, define una variable que liste las columnas en las que realmente te interesa:

```python
>>> select = ['name','shares', 'price']
>>>
```

Ahora, localiza los índices de las columnas anteriores en el archivo CSV de origen:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Finalmente, lee una fila de datos y conviértela en un diccionario utilizando una comprensión de diccionario:

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Si te sientes cómodo con lo que acaba de suceder, lee el resto del archivo:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

Oh, mira, acabas de reducir gran parte de la función `read_portfolio()` a una sola instrucción.
