# Mejora de la implementación de descriptores

En este paso, vamos a mejorar nuestra implementación de descriptores. Es posible que hayas notado que en algunos casos, hemos estado especificando nombres de forma redundante. Esto puede hacer que nuestro código sea un poco desordenado y más difícil de mantener. Para resolver este problema, usaremos el método `__set_name__`, una función útil introducida en Python 3.6.

El método `__set_name__` se llama automáticamente cuando se define la clase. Su función principal es establecer el nombre del descriptor por nosotros, por lo que no tenemos que hacerlo manualmente cada vez. Esto hará que nuestro código sea más limpio y eficiente.

Ahora, actualicemos el archivo `validate.py` para incluir el método `__set_name__`. Así es como se verá el código actualizado:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
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

En el código anterior, el método `__set_name__` en la clase `Validator` comprueba si el atributo `name` es `None`. Si lo es, establece el `name` al nombre del atributo real utilizado en la definición de la clase. De esta manera, no tenemos que especificar el nombre explícitamente cuando creamos instancias de las clases de descriptores.

Ahora que hemos actualizado el archivo `validate.py`, podemos crear una versión mejorada de nuestra clase `Stock`. Esta nueva versión no requerirá que especifiquemos los nombres de forma redundante. Aquí está el código para la clase `Stock` mejorada:

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

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

En esta clase `Stock`, simplemente creamos instancias de las clases de descriptores `String`, `PositiveInteger` y `PositiveFloat` sin especificar los nombres. El método `__set_name__` en la clase `Validator` se encargará de establecer los nombres automáticamente.

Probemos nuestra clase `Stock` mejorada. Primero, abre tu terminal y navega hasta el directorio del proyecto. Luego, ejecuta el archivo `improved_stock.py` en modo interactivo. Aquí están los comandos para hacerlo:

```bash
cd ~/project
python3 -i improved_stock.py
```

Una vez que estés en la sesión interactiva de Python, puedes probar los siguientes comandos para probar la funcionalidad de la clase `Stock`:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

Estos comandos crean una instancia de la clase `Stock`, imprimen sus atributos, cambian el valor de un atributo y luego intentan establecer valores no válidos para ver si se generan los errores adecuados.

El método `__set_name__` establece automáticamente el nombre del descriptor cuando se define la clase. Esto hace que tu código sea más limpio y menos redundante, ya que ya no necesitas especificar el nombre del atributo dos veces.

Esta mejora demuestra cómo el protocolo de descriptores de Python sigue evolucionando, lo que facilita escribir código limpio y mantenible.
