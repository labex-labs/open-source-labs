# Variables de clase y herencia

Las variables de clase como `types` a veces se usan como un mecanismo de personalización cuando se utiliza la herencia. Por ejemplo, en la clase `Stock`, los tipos se pueden cambiar fácilmente en una subclase. Prueba este ejemplo que cambia el atributo `price` a una instancia de `Decimal` (que a menudo es más adecuado para cálculos financieros):

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**Discusión sobre el diseño**

El problema que se aborda en este laboratorio concierne a la conversión de datos leídos de un archivo. ¿Tendría sentido realizar estas conversiones en el método `__init__()` de la clase `Stock` en lugar de eso? Por ejemplo:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Al hacer esto, convertirías una fila de datos de la siguiente manera:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

¿Es esto bueno o malo? ¿Cuáles son tus pensamientos? En general, creo que es un diseño cuestionable ya que mezcla dos cosas diferentes: la creación de una instancia y la conversión de datos. Además, las conversiones implícitas en `__init__()` limitan la flexibilidad y pueden introducir errores extraños si un usuario no presta atención cuidadosamente.
