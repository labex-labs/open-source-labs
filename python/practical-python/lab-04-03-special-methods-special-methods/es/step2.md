# Métodos especiales para conversiones de cadenas

Los objetos tienen dos representaciones en forma de cadena.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

La función `str()` se utiliza para crear una salida imprimible agradable:

```python
>>> str(d)
'2012-12-21'
>>>
```

La función `repr()` se utiliza para crear una representación más detallada para los programadores.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Esas funciones, `str()` y `repr()`, utilizan un par de métodos especiales en la clase para producir la cadena que se va a mostrar.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Utilizado con `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Utilizado con `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_Nota: La convención para `__repr__()` es devolver una cadena que, cuando se le pasa a `eval()`, volverá a crear el objeto subyacente. Si esto no es posible, se utiliza en su lugar una representación fácil de leer._
