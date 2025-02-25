# Operaciones comunes

Para obtener valores de un diccionario, use los nombres de las claves.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

Para agregar o modificar valores, asigne usando los nombres de las claves.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

Para eliminar un valor, use la instrucción `del`.

```python
>>> del s['date']
>>>
```
