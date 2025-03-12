# Aplicando Validadores a una Clase de Acciones

En este paso, veremos cómo funcionan nuestros validadores en una situación del mundo real. Los validadores son como pequeños verificadores que se aseguran de que los datos que utilizamos cumplan con ciertas reglas. Crearemos una clase `Stock`. Una clase es como un plano para crear objetos. En este caso, la clase `Stock` representará una acción en el mercado de valores, y usaremos nuestros validadores para asegurarnos de que los valores de sus atributos (como el número de acciones y el precio) sean válidos.

## Creando la Clase de Acciones

Primero, necesitamos crear un nuevo archivo. En el WebIDE, crea un nuevo archivo llamado `stock.py`. Este archivo contendrá el código para nuestra clase `Stock`. Ahora, agrega el siguiente código al archivo `stock.py`:

```python
# stock.py
from validate import PositiveInteger, PositiveFloat

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    def cost(self):
        return self.shares * self.price
```

Analicemos lo que hace este código:

1. Comenzamos importando los validadores `PositiveInteger` y `PositiveFloat` de nuestro módulo `validate`. Estos validadores nos ayudarán a asegurarnos de que el número de acciones sea un entero positivo y el precio sea un número decimal positivo.
2. Luego definimos una clase `Stock`. Dentro de la clase, tenemos un método `__init__`. Este método se llama cuando creamos un nuevo objeto `Stock`. Toma tres parámetros: `name`, `shares` y `price`, y los asigna a los atributos del objeto.
3. Usamos propiedades y setters para validar los valores de `shares` y `price`. Una propiedad es una forma de controlar el acceso a un atributo, y un setter es un método que se llama cuando intentamos establecer el valor de ese atributo. Cuando establecemos el atributo `shares`, se llama al método `PositiveInteger.check` para asegurarnos de que el valor sea un entero positivo. Del mismo modo, cuando establecemos el atributo `price`, se llama al método `PositiveFloat.check` para asegurarnos de que el valor sea un número decimal positivo.
4. Finalmente, tenemos un método `cost`. Este método calcula el costo total de la acción multiplicando el número de acciones por el precio.

## Probando la Clase de Acciones

Ahora que hemos creado nuestra clase `Stock`, necesitamos probarla para ver si los validadores funcionan correctamente. Abre una nueva terminal y inicia el intérprete de Python. Puedes hacer esto ejecutando el siguiente comando:

```bash
python3
```

Una vez que el intérprete de Python esté en funcionamiento, podemos importar y probar nuestra clase `Stock`. Ingresa el siguiente código en el intérprete de Python:

```python
from stock import Stock

# Create a valid stock
s = Stock('GOOG', 100, 490.10)
print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try setting an invalid shares value
try:
    s.shares = -10
except ValueError as e:
    print(f"Error setting shares: {e}")

# Try setting an invalid price value
try:
    s.price = "not a price"
except TypeError as e:
    print(f"Error setting price: {e}")
```

Cuando ejecutes este código, deberías ver una salida similar a la siguiente:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Error setting shares: Expected >= 0
Error setting price: Expected <class 'float'>
```

Esta salida muestra que nuestros validadores funcionan como se esperaba. La clase `Stock` no nos permite establecer valores inválidos para `shares` y `price`. Cuando intentamos establecer un valor inválido, se genera un error, y podemos capturar e imprimir ese error.

## Entendiendo Cómo Ayuda la Herencia

Una de las grandes ventajas de usar nuestros validadores es que podemos combinar fácilmente diferentes reglas de validación. La herencia es un concepto poderoso en Python que nos permite crear nuevas clases basadas en las existentes. Con la herencia múltiple, podemos usar la función `super()` para llamar a métodos de múltiples clases padre.

Por ejemplo, si queremos asegurarnos de que el nombre de la acción no esté vacío, podemos seguir estos pasos:

1. Importar el validador `NonEmptyString` del módulo `validate`. Este validador nos ayudará a comprobar si el nombre de la acción no es una cadena vacía.
2. Agregar un setter de propiedad para el atributo `name` en la clase `Stock`. Este setter usará el método `NonEmptyString.check()` para validar el nombre de la acción.

Esto muestra cómo la herencia, especialmente la herencia múltiple con la función `super()`, nos permite construir componentes flexibles y reutilizables en diferentes combinaciones.

Cuando hayas terminado de probar, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
exit()
```
