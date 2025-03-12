# Clausuras como un Generador de Código

En este paso, aprenderemos cómo se pueden utilizar las clausuras (closures) para generar código de forma dinámica. En concreto, construiremos un sistema de comprobación de tipos (type-checking) para atributos de clase utilizando clausuras.

Primero, entendamos qué son las clausuras. Una clausura es un objeto función que recuerda los valores en el ámbito envolvente incluso si no están presentes en la memoria. En Python, las clausuras se crean cuando una función anidada hace referencia a un valor de su función envolvente.

Ahora, comenzaremos a implementar nuestro sistema de comprobación de tipos.

1. Crea un nuevo archivo llamado `typedproperty.py` en el directorio `/home/labex/project` con el siguiente código:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
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

En este código, la función `typedproperty` es una clausura. Toma dos argumentos: `name` y `expected_type`. El decorador `@property` se utiliza para crear un método getter para la propiedad, que recupera el valor del atributo privado. El decorador `@value.setter` crea un método setter que comprueba si el valor que se está estableciendo es del tipo esperado. Si no lo es, levanta una excepción `TypeError`.

2. Ahora, creemos una clase que utilice estas propiedades con comprobación de tipos. Crea un archivo llamado `stock.py` con el siguiente código:

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

En la clase `Stock`, utilizamos la función `typedproperty` para crear atributos con comprobación de tipos para `name`, `shares` y `price`. Cuando creamos una instancia de la clase `Stock`, la comprobación de tipos se aplicará automáticamente.

3. Creemos un archivo de prueba para ver esto en acción. Crea un archivo llamado `test_stock.py` con el siguiente código:

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

En este archivo de prueba, primero creamos un objeto `Stock` con los tipos correctos. Luego intentamos establecer el atributo `shares` a una cadena, lo que debería levantar una excepción `TypeError` porque el tipo esperado es un entero.

4. Ejecuta el archivo de prueba:

```bash
python3 test_stock.py
```

Deberías ver una salida similar a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

Esta salida muestra que la comprobación de tipos está funcionando correctamente.

5. Ahora, mejoraremos `typedproperty.py` agregando funciones de conveniencia para tipos comunes. Agrega el siguiente código al final del archivo:

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

Estas funciones son simplemente envoltorios (wrappers) alrededor de la función `typedproperty`, lo que facilita la creación de propiedades de tipos comunes.

6. Crea un nuevo archivo llamado `stock_enhanced.py` que utilice estas funciones de conveniencia:

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Esta clase `Stock` utiliza las funciones de conveniencia para crear atributos con comprobación de tipos, lo que hace que el código sea más legible.

7. Crea un archivo de prueba `test_stock_enhanced.py` para probar la versión mejorada:

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Este archivo de prueba es similar al anterior, pero prueba la clase `Stock` mejorada.

8. Ejecuta la prueba:

```bash
python3 test_stock_enhanced.py
```

Deberías ver una salida similar a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

En este paso, hemos demostrado cómo se pueden utilizar las clausuras para generar código. La función `typedproperty` crea objetos de propiedad que realizan comprobación de tipos, y las funciones `String`, `Integer` y `Float` crean propiedades especializadas para tipos comunes.
