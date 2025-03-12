# Crear una clase base de estructura

Ahora que tenemos una buena comprensión del paso de argumentos de funciones, vamos a crear una clase base reutilizable para estructuras de datos. Este paso es crucial porque nos ayuda a evitar escribir el mismo código una y otra vez cuando creamos clases simples que almacenan datos. Al utilizar una clase base, podemos optimizar nuestro código y hacerlo más eficiente.

## El problema con el código repetitivo

En los ejercicios anteriores, definiste una clase `Stock` como se muestra a continuación:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Observa detenidamente el método `__init__`. Notarás que es bastante repetitivo. Tienes que asignar manualmente cada atributo uno por uno. Esto puede volverse muy tedioso y consumir mucho tiempo, especialmente cuando tienes muchas clases con una gran cantidad de atributos.

## Crear una clase base flexible

Vamos a crear una clase base `Structure` que pueda manejar automáticamente la asignación de atributos. Primero, abre el WebIDE y crea un nuevo archivo llamado `structure.py`. Luego, agrega el siguiente código a este archivo:

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

Esta clase base tiene varias características importantes:

1. Define una variable de clase `_fields`. Por defecto, esta variable está vacía. Esta variable contendrá los nombres de los atributos que tendrá la clase.
2. Comprueba si el número de argumentos pasados al constructor coincide con el número de campos definidos en `_fields`. Si no coinciden, genera un `TypeError`. Esto nos ayuda a detectar errores temprano.
3. Establece los atributos del objeto utilizando los nombres de los campos y los valores proporcionados como argumentos. La función `setattr` se utiliza para establecer dinámicamente los atributos.

## Probar nuestra clase base de estructura

Ahora, vamos a crear algunas clases de ejemplo que heredan de la clase base `Structure`. Agrega el siguiente código a tu archivo `structure.py`:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

Para probar si nuestra implementación funciona correctamente, crearemos un archivo de prueba llamado `test_structure.py`. Agrega el siguiente código a este archivo:

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Para ejecutar la prueba, abre tu terminal y ejecuta el siguiente comando:

```bash
python3 test_structure.py
```

Deberías ver la siguiente salida:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Como puedes ver, nuestra clase base está funcionando como se esperaba. Ha hecho que sea mucho más fácil definir nuevas estructuras de datos sin tener que escribir el mismo código de plantilla repetidamente.
