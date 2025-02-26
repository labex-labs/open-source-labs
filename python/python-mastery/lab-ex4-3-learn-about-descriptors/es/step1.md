# Descriptores en acción

Antes, creaste una clase `Stock` que utilizaba slots, propiedades y otras características. Todas estas características se implementan utilizando el protocolo de descriptores. Vea cómo funciona intentando este experimento simple.

Primero, cree un objeto de stock y trate de buscar algunos atributos:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

Ahora, observe que estos atributos se encuentran en el diccionario de la clase.

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price','shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

Intente estos pasos que ilustran cómo los descriptores obtienen y establecen valores en una instancia:

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: Expected an integer
>>>
```

La ejecución de `__get__()` y `__set__()` ocurre automáticamente cada vez que se accede a las instancias.
