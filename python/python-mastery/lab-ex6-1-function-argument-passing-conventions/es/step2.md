# Estructuras de datos simplificadas

En ejercicios anteriores, definiste una clase que representa una acción de la siguiente manera:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Presta atención al método `__init__()`: ¿no es una gran cantidad de código para escribir cada vez que quieres poblar una estructura? ¿Qué pasaría si tuvieras que definir docenas de tales estructuras en tu programa?

En un archivo `structure.py`, define una clase base `Structure` que permita al usuario definir estructuras de datos simples de la siguiente manera:

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

La clase `Structure` debe definir un método `__init__()` que tome cualquier número de argumentos y que busque la presencia de una variable de clase `_fields`. Haga que el método poble la instancia a partir de los nombres de atributo en `_fields` y los valores pasados a `__init__()`.

A continuación, hay un código de muestra para probar tu implementación:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
