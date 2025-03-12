# Eliminando Nombres de Propiedades con Descriptores

En el paso anterior, al crear propiedades tipadas, tuvimos que declarar explícitamente los nombres de las propiedades. Esto es redundante porque los nombres de las propiedades ya se especifican en la definición de la clase. En este paso, usaremos descriptores para eliminar esta redundancia.

Un descriptor en Python es un objeto especial que controla cómo funciona el acceso a los atributos. Cuando se implementa el método `__set_name__` en un descriptor, este puede capturar automáticamente el nombre del atributo de la definición de la clase.

Comencemos creando un nuevo archivo.

1. Crea un nuevo archivo llamado `improved_typedproperty.py` con el siguiente código:

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

Este código define una clase descriptor llamada `TypedProperty` que comprueba el tipo de los valores asignados a los atributos. El método `__set_name__` se llama automáticamente cuando el descriptor se asigna a un atributo de clase. Esto permite que el descriptor capture el nombre del atributo sin que tengamos que especificarlo manualmente.

A continuación, crearemos una clase que utilice estas propiedades tipadas mejoradas.

2. Crea un nuevo archivo llamado `stock_improved.py` que utilice las propiedades tipadas mejoradas:

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Observa que no es necesario especificar los nombres de las propiedades al crear las propiedades tipadas. El descriptor obtendrá automáticamente el nombre del atributo de la definición de la clase.

Ahora, probemos nuestra clase mejorada.

3. Crea un archivo de prueba `test_stock_improved.py` para probar la versión mejorada:

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Finalmente, ejecutaremos la prueba para ver si todo funciona como se espera.

4. Ejecuta la prueba:

```bash
python3 test_stock_improved.py
```

Deberías ver una salida similar a:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

En este paso, hemos mejorado nuestro sistema de comprobación de tipos utilizando descriptores y el método `__set_name__`. Esto elimina la especificación redundante del nombre de la propiedad, lo que hace que el código sea más corto y menos propenso a errores.

El método `__set_name__` es una característica muy útil de los descriptores. Permite que recopilen automáticamente información sobre cómo se utilizan en una definición de clase. Esto se puede utilizar para crear APIs más fáciles de entender y usar.
