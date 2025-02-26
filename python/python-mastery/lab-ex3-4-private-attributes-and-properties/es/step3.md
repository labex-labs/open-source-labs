# Aplicando reglas de validación

Utilizando propiedades y atributos privados, modifica el atributo `shares` de la clase `Stock` de modo que solo se pueda asignar un valor entero no negativo. Además, modifica el atributo `price` de modo que solo se pueda asignar un valor de punto flotante no negativo.

El nuevo objeto debe funcionar casi exactamente igual que el antiguo, excepto por la comprobación adicional de tipos y valores.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # OK
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: Expected integer
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: shares must be >= 0

>>> s.price = 123.45       # OK
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: Expected float
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: price must be >= 0
>>>
```
