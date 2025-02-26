# Ejercicio 4.2: Agregando algunos métodos

Con las clases, puedes adjuntar funciones a tus objetos. Estas se conocen como métodos y son funciones que operan sobre los datos almacenados dentro de un objeto. Agrega un método `cost()` y `sell()` a tu objeto `Stock`. Deberían funcionar así:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```
