# Crecimiento de diccionarios/clases

Los diccionarios de Python (y las clases) permiten almacenar hasta 5 valores antes de que su memoria reservada se duplique. Investigue creando un diccionario y agregando algunos más valores a él:

```python
>>> row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
>>> sys.getsizeof(row)
>>> sys.getsizeof(row)
240
>>> row['a'] = 1
>>> sys.getsizeof(row)
240
>>> row['b'] = 2
>>> sys.getsizeof(row)
368
>>>
```

¿Baja la memoria si elimina el elemento que acaba de agregar?

Pensamiento al respecto: Si está creando un gran número de registros, representar cada registro como un diccionario puede no ser el enfoque más eficiente: podría estar pagando un precio elevado por la conveniencia de tener un diccionario. Podría ser mejor considerar el uso de tuplas, tuplas con nombres o clases que definen `__slots__`.
