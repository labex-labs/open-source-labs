# Ahorrando mucha memoria

En el Ejercicio 2.1 escribiste una función `read_rides_as_dicts()` que lee los datos del autobús CTA en una lista de diccionarios. Usarlo requiere mucha memoria. Por ejemplo, encontremos el día en el que el autobús de la ruta 22 tuvo la mayor cantidad de pasajeros:

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... mira el resultado. Debería ser de alrededor de 220MB
>>>
```

Ahora, intentemos un ejemplo que involucre generadores. Reinicia Python y prueba esto:

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... mira el resultado. Debería ser MUCHÍSIMO más pequeño que antes
>>>
```

Tien en cuenta que acabas de procesar todo el conjunto de datos como si estuviera almacenado como una secuencia de diccionarios. Sin embargo, en ningún momento creaste y almacenaste realmente una lista de diccionarios. No todos los problemas se pueden estructurar de esta manera, pero si puedes trabajar con los datos de manera iterativa, las expresiones generadoras pueden ahorrar una cantidad enorme de memoria.
