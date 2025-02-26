# Ejercicio 5.6: Propiedades simples

Las propiedades son una forma útil de agregar "atributos calculados" a un objeto. En `stock.py`, creaste un objeto `Stock`. Observa que en tu objeto hay una ligera inconsistencia en cómo se extraen diferentes tipos de datos:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

En particular, observa cómo tienes que agregar los paréntesis extra a `cost` porque es un método.

Puedes eliminar los paréntesis extra en `cost()` si lo conviertes en una propiedad. Toma tu clase `Stock` y modifíquela de modo que el cálculo del costo funcione así:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Intenta llamar a `s.cost()` como una función y observa que ya no funciona ahora que `cost` se ha definido como una propiedad.

```python
>>> s.cost()
... falla...
>>>
```

Hacer este cambio probablemente romperá tu programa `pcost.py` anterior. Es posible que tengas que volver y eliminar los paréntesis del método `cost()`.
