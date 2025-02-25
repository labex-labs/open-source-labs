# Ejercicio 1.25: Listas de cualquier cosa

Las listas pueden contener cualquier tipo de objeto, incluyendo otras listas (por ejemplo, listas anidadas). Prueba esto:

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Presta atención detenidamente a la salida anterior. `items` es una lista con tres elementos. El primer elemento es una cadena de texto, pero los otros dos elementos son listas.

Puedes acceder a los elementos de las listas anidadas mediante múltiples operaciones de indexación.

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Aunque técnicamente es posible crear estructuras de lista muy complicadas, como regla general, quieres mantener las cosas simples. Por lo general, las listas contienen elementos que son todos del mismo tipo de valor. Por ejemplo, una lista que consta enteramente de números o una lista de cadenas de texto. Mezclar diferentes tipos de datos en la misma lista a menudo es una buena manera de hacer que te desborden los sesos, por lo que es mejor evitarlo.
