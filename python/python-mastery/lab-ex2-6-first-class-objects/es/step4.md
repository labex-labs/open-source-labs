# Proyecto de desafío especial

En el Ejercicio 2.5, creamos una clase `RideData` que almacenaba todos los datos del autobús en columnas, pero en realidad presentaba los datos a un usuario como una secuencia de diccionarios. Ahorró mucha memoria a través de diversas formas de magia.

¿Puedes generalizar esa idea? Específicamente, ¿puedes crear una función general `read_csv_as_columns()` que funcione así:

```python
>>> data = read_csv_as_columns('ctabus.csv', types=[str, str, str, int])
>>> data
<__main__.DataCollection object at 0x102b45048>
>>> len(data)
577563
>>> data[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> data[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Esta función está destinada a ser general: puedes darle cualquier archivo y una lista de los tipos de columna y leerá los datos. Los datos se leen en una clase `DataCollection` que almacena los datos como columnas internamente. Sin embargo, los datos se presentan como una secuencia de diccionarios cuando se acceden.

Intenta usar esta función con el truco de la internación de cadenas en la última parte. ¿Cuánta memoria se necesita para almacenar todos los datos de viaje ahora? ¿Puedes seguir usando esta función con tu código de análisis de CTA anterior?

## Nota:

Completa la función `read_csv_as_columns()` en el archivo `colreader.py`.
