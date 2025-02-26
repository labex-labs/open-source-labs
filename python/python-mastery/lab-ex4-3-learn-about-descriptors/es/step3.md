# De Validadores a Descriptores

En el ejercicio anterior, escribiste una serie de clases que podían realizar comprobaciones. Por ejemplo:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: expected <class 'int'>
>>> PositiveInteger.check(-10)
```

Puedes extender esto a descriptores con un simple cambio en la clase base `Validator`. Cambia la clase a la siguiente:

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Nota: La ausencia del método `__get__()` en el descriptor significa que Python usará su implementación predeterminada de búsqueda de atributos. Esto requiere que el nombre suministrado coincida con el nombre utilizado en el diccionario de instancia.

No debería ser necesario hacer otros cambios. Ahora, intenta modificar la clase `Stock` para usar los validadores como descriptores de la siguiente manera:

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Verás que tu clase funciona de la misma manera que antes, tiene mucho menos código y te da todas las comprobaciones deseadas:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError...
>>> s.shares = -50
... ValueError...
>>>
```

Esto es bastante genial. Los descriptores te han permitido simplificar en gran medida la implementación de la clase `Stock`. Esta es la verdadera fuerza de los descriptores: obtienes un control de bajo nivel sobre el operador de punto y puedes utilizarlo para hacer cosas sorprendentes.
