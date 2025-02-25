# Ejercicio 2.17: Invertir un diccionario

Un diccionario mapea claves a valores. Por ejemplo, un diccionario de precios de acciones.

```python
>>> prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }
>>>
```

Si usas el método `items()`, puedes obtener pares `(clave,valor)`:

```python
>>> prices.items()
dict_items([('GOOG', 490.1), ('AA', 23.45), ('IBM', 91.1), ('MSFT', 34.23)])
>>>
```

Sin embargo, ¿y si quisieras obtener una lista de pares `(valor, clave)` en lugar de eso? _Pista: usa `zip()`._

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

¿Por qué harías esto? En primer lugar, te permite realizar ciertos tipos de procesamiento de datos en los datos del diccionario.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

Esto también ilustra una característica importante de las tuplas. Cuando se usan en comparaciones, las tuplas se comparan elemento a elemento, comenzando con el primer elemento. Similar a la forma en que se comparan las cadenas carácter a carácter.

`zip()` se usa a menudo en situaciones como esta donde necesitas emparejar datos de diferentes lugares. Por ejemplo, emparejar los nombres de columna con los valores de columna para crear un diccionario de valores con nombre.

Tenga en cuenta que `zip()` no está limitado a pares. Por ejemplo, puedes usarlo con cualquier número de listas de entrada:

```python
>>> a = [1, 2, 3, 4]
>>> b = ['w', 'x', 'y', 'z']
>>> c = [0.2, 0.4, 0.6, 0.8]
>>> list(zip(a, b, c))
[(1, 'w', 0.2), (2, 'x', 0.4), (3, 'y', 0.6), (4, 'z', 0.8))]
>>>
```

También, tenga en cuenta que `zip()` se detiene una vez que la secuencia de entrada más corta se agota.

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = ['x', 'y', 'z']
>>> list(zip(a,b))
[(1, 'x'), (2, 'y'), (3, 'z')]
>>>
```
