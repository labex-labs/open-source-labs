# Los closures como generador de código

En el Ejercicio 4.3, desarrollaste una colección de clases descriptoras que permitían la comprobación de tipos de los atributos de los objetos. Por ejemplo:

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

Este tipo de cosas también se puede implementar utilizando closures. Crea un archivo `typedproperty.py` y pon el siguiente código en él:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Esto parece bastante salvaje, pero la función está efectivamente creando código. Lo usarías en una definición de clase de la siguiente manera:

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

Verifica que esta clase realice la comprobación de tipos de la misma manera que el código de descriptores.

Agrega las funciones `String()`, `Integer()` y `Float()` al archivo `typedproperty.py` para que puedas escribir el siguiente código:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
