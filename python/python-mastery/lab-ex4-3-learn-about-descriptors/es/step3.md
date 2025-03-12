# Implementación de validadores utilizando descriptores

En este paso, vamos a crear un sistema de validación utilizando descriptores. Pero primero, entendamos qué son los descriptores y por qué los estamos utilizando. Los descriptores son objetos de Python que implementan el protocolo de descriptores, que incluye los métodos `__get__`, `__set__` o `__delete__`. Permiten personalizar cómo se accede, se establece o se elimina un atributo en un objeto. En nuestro caso, usaremos descriptores para crear un sistema de validación que asegure la integridad de los datos. Esto significa que los datos almacenados en nuestros objetos siempre cumplirán ciertos criterios, como ser de un tipo específico o tener un valor positivo.

Ahora, comencemos a crear nuestro sistema de validación. Crearemos un nuevo archivo llamado `validate.py` en el directorio del proyecto. Este archivo contendrá las clases que implementan nuestros validadores.

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


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

En el archivo `validate.py`, primero definimos una clase base llamada `Validator`. Esta clase tiene un método `__init__` que toma un parámetro `name`, que se utilizará para identificar el atributo que se está validando. El método `check` es un método de clase que simplemente devuelve el valor pasado a él. El método `__set__` es un método de descriptor que se llama cuando se establece un atributo en un objeto. Llama al método `check` para validar el valor y luego almacena el valor validado en el diccionario del objeto.

Luego definimos tres subclases de `Validator`: `String`, `PositiveInteger` y `PositiveFloat`. Cada una de estas subclases anula el método `check` para realizar comprobaciones de validación específicas. La clase `String` comprueba si el valor es una cadena, la clase `PositiveInteger` comprueba si el valor es un entero positivo y la clase `PositiveFloat` comprueba si el valor es un número positivo (ya sea un entero o un flotante).

Ahora que tenemos definidos nuestros validadores, modifiquemos nuestra clase `Stock` para utilizar estos validadores. Crearemos un nuevo archivo llamado `stock_with_validators.py` e importaremos los validadores del archivo `validate.py`.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

En el archivo `stock_with_validators.py`, definimos la clase `Stock` y utilizamos los validadores como atributos de clase. Esto significa que cada vez que se establece un atributo en un objeto `Stock`, se llamará al método `__set__` del validador correspondiente para validar el valor. El método `__init__` inicializa los atributos del objeto `Stock`, y los métodos `cost`, `sell` y `__repr__` proporcionan funcionalidad adicional.

Ahora, probemos nuestra clase `Stock` basada en validadores. Abramos una terminal, naveguemos hasta el directorio del proyecto y ejecutemos el archivo `stock_with_validators.py` en modo interactivo.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Una vez que el intérprete de Python esté en ejecución, podemos probar algunos comandos para probar el sistema de validación.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

En el código de prueba, primero creamos un objeto `Stock` con valores válidos e imprimimos sus atributos para verificar que se hayan establecido correctamente. Luego intentamos cambiar el atributo `shares` a un valor válido e imprimimos de nuevo para confirmar el cambio. Finalmente, intentamos establecer el atributo `shares` a un valor no válido (una cadena y un número negativo) y capturamos las excepciones que lanzan los validadores.

Observa lo mucho más limpio que es nuestro código ahora. La clase `Stock` ya no necesita implementar todos esos métodos de propiedad; los validadores se encargan de todas las comprobaciones de tipo y restricciones.

Los descriptores nos han permitido crear un sistema de validación reutilizable que se puede aplicar a cualquier atributo de clase. Este es un patrón poderoso para mantener la integridad de los datos en toda tu aplicación.
