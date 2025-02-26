# Slots vs. setattr

En ejercicios anteriores, `__slots__` se utilizó para enumerar los atributos de instancia en una clase. El propósito principal de los slots es optimizar el uso de memoria. Un efecto secundario es que limita estrictamente los atributos permitidos a los enumerados. Una desventaja de los slots es que a menudo interactúa extrañamente con otras partes de Python (por ejemplo, las clases que usan slots no se pueden usar con la herencia múltiple). Por esa razón, realmente no deberías usar slots excepto en casos especiales.

Si realmente quisieras limitar el conjunto de atributos permitidos, una forma alternativa de hacerlo sería definir un método `__setattr__()`. Intenta este experimento:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name','shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

En este ejemplo, no hay slots, pero el método `__setattr__()` todavía restringe los atributos a aquellos en un conjunto predefinido. Probablemente tendrías que pensar en cómo este enfoque podría interactuar con la herencia (por ejemplo, si las subclases quisieran agregar nuevos atributos, probablemente tendrían que redefinir `__setattr__()` para que funcione).
