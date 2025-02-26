# Tuplas con Nombres

En el Ejercicio 2.1, experimentó con objetos `namedtuple` en el módulo `collections`. Solo para refrescar su memoria, aquí está cómo funcionaban:

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

En el fondo, la función `namedtuple()` está creando código como una cadena y lo está ejecutando utilizando `exec()`. Mire el código y admiré:

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... mire la salida...
>>>
```
