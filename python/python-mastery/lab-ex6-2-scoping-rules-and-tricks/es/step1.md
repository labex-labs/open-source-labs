# Preparación

En el último ejercicio, creaste una clase `Structure` que facilitó la definición de estructuras de datos. Por ejemplo:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

Esto funciona bien, excepto que muchas cosas son bastante extrañas en la función `__init__()`. Por ejemplo, si pides ayuda usando `help(Stock)`, no obtienes ningún tipo de firma útil. Además, la pasaje de argumentos con palabras clave no funciona. Por ejemplo:

```python
>>> help(Stock)
... mira la salida...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() got an unexpected keyword argument 'price'
>>>
```

En este ejercicio, vamos a ver un enfoque diferente para este problema.
