# Ejercicio 2.25: Creando diccionarios

Recuerda cómo la función `dict()` puede crear fácilmente un diccionario si tienes una secuencia de nombres de claves y valores? Vamos a crear un diccionario a partir de los encabezados de columna:

```python
>>> headers
['name','shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```

Por supuesto, si estás versado en comprensiones de listas, puedes hacer toda la conversión en un solo paso usando una comprensión de diccionario:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```
