# Ejercicio 5.7: Propiedades y setters

Modifica el atributo `shares` de modo que el valor se almacene en un atributo privado y que se utilicen un par de funciones de propiedad para garantizar que siempre se establezca en un valor entero. Aquí hay un ejemplo del comportamiento esperado:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
