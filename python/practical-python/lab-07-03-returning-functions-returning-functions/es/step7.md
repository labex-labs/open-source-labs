# Ejercicio 7.7: Usar Cerraduras para Evitar la Repetición

Una de las características más poderosas de las cerraduras es su uso en la generación de código repetitivo. Si se vuelve a revisar el Ejercicio 5.7, recuerde el código para definir una propiedad con comprobación de tipos.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

En lugar de escribir repetidamente ese código una y otra vez, se puede crear automáticamente utilizando una cerradura.

Cree un archivo `typedproperty.py` y coloque el siguiente código en él:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Ahora, pruébelo definiendo una clase como esta:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Intente crear una instancia y verificar que la comprobación de tipos funcione.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... debería obtener un TypeError...
>>>
```
