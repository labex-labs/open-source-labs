# Propiedades para atributos calculados

Antes, definiste una clase `Stock`. Por ejemplo:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Utilizando una propiedad, convierte `cost()` en un atributo que ya no requiera paréntesis. Por ejemplo:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost               # Propiedad. Calcula el costo
49010.0
>>>
```
