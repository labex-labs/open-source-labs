# Desafío

¿Qué pasa cuando se toma una porción de datos de viajes?

```python
>>> r = rows[0:10]
>>> r
... mira el resultado...
>>>
```

Probablemente se verá un poco loco. ¿Puedes modificar la clase `RideData` para que produzca una porción adecuada que se vea como una lista de diccionarios? Por ejemplo, así:

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
