# Depuración con Print

La depuración con `print()` es bastante común.

_Consejo: Asegúrate de usar `repr()`_

```python
def spam(x):
    print('DEBUG:', repr(x))
  ...
```

`repr()` muestra una representación exacta de un valor. No la salida de impresión _bonita_.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# SIN `repr`
>>> print(x)
3.4
# CON `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
