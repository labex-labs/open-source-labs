# El sorprendente poder de la iteración

Python utiliza la iteración de maneras que quizás no esperes. Una vez que hayas agregado `__iter__()` a la clase `Structure`, encontrarás que es fácil realizar todo tipo de nuevas operaciones. Por ejemplo, conversiones a secuencias y desempaquetado:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

Mientras estamos en ello, ahora podemos agregar un operador de comparación a nuestra clase `Structure`:

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

Ahora deberías poder comparar objetos:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

Intenta ejecutar nuevamente tus pruebas unitarias `teststock.py`. Ahora todo debería pasar. Excelente.
