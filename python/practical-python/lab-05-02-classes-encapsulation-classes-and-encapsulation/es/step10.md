# Atributo `__slots__`

Puedes restringir el conjunto de nombres de atributos.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

Generará un error para otros atributos.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' object has no attribute 'prices'
```

Aunque esto evita errores y restringe el uso de objetos, en realidad se utiliza para mejorar el rendimiento y hacer que Python utilice la memoria de manera más eficiente.
