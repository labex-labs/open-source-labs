# Ejercicio 2.3: Algunas operaciones adicionales de diccionarios

Si conviertes un diccionario en una lista, obtendrás todas sus claves:

```python
>>> list(d)
['name','shares', 'price', 'date', 'account']
>>>
```

Del mismo modo, si usas la instrucción `for` para iterar sobre un diccionario, obtendrás las claves:

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Prueba esta variante que realiza una búsqueda al mismo tiempo:

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

También puedes obtener todas las claves usando el método `keys()`:

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name','shares', 'price', 'date', 'account'])
>>>
```

`keys()` es un poco inusual en que devuelve un objeto especial `dict_keys`.

Este es una superposición sobre el diccionario original que siempre te da las claves actuales, incluso si el diccionario cambia. Por ejemplo, prueba esto:

```python
>>> del d['account']
>>> keys
dict_keys(['name','shares', 'price', 'date'])
>>>
```

Observa cuidadosamente que `'account'` desapareció de `keys` aunque no llamaste a `d.keys()` nuevamente.

Una forma más elegante de trabajar con claves y valores juntos es usar el método `items()`. Esto te da tuplas `(clave, valor)`:

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

Si tienes tuplas como `items`, puedes crear un diccionario usando la función `dict()`. Prueba:

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
