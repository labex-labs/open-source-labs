# Implementación de la verificación de tipos con descriptores

En este paso, vamos a crear una clase `Stock` que utiliza descriptores para la verificación de tipos. Pero primero, entendamos qué son los descriptores. Los descriptores son una característica realmente poderosa en Python. Te dan control sobre cómo se accede a los atributos en las clases.

Los descriptores son objetos que definen cómo se accede a los atributos en otros objetos. Lo hacen implementando métodos especiales como `__get__`, `__set__` y `__delete__`. Estos métodos permiten a los descriptores gestionar cómo se recuperan, establecen y eliminan los atributos. Los descriptores son muy útiles para implementar validación, verificación de tipos y propiedades calculadas. Por ejemplo, puedes usar un descriptor para asegurarte de que un atributo siempre sea un número positivo o una cadena de un cierto formato.

El archivo `validate.py` ya tiene clases validadoras (`String`, `PositiveInteger`, `PositiveFloat`). Podemos usar estas clases para validar los atributos de nuestra clase `Stock`.

Ahora, creemos nuestra clase `Stock` con descriptores.

1. Primero, abre el archivo `stock.py` en el editor. Puedes hacer esto ejecutando el siguiente comando en tu terminal:

```bash
code ~/project/stock.py
```

Este comando utiliza el editor `code` para abrir el archivo `stock.py` ubicado en el directorio `~/project`.

2. Una vez abierto el archivo, reemplaza el contenido de marcador de posición con el siguiente código:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Analicemos lo que hace este código. La tupla `_fields` define los atributos de la clase `Stock`. Estos son los nombres de los atributos que tendrán nuestros objetos `Stock`.

Los atributos `name`, `shares` y `price` se definen como objetos descriptor. El descriptor `String()` asegura que el atributo `name` sea una cadena. El descriptor `PositiveInteger()` se asegura de que el atributo `shares` sea un entero positivo. Y el descriptor `PositiveFloat()` garantiza que el atributo `price` sea un número de punto flotante positivo.

La propiedad `cost` es una propiedad calculada. Calcula el costo total de la acción en función del número de acciones y el precio por acción.

El método `sell` se utiliza para reducir el número de acciones. Cuando llamas a este método con un número de acciones para vender, resta ese número del atributo `shares`.

La línea `Stock.create_init()` crea dinámicamente un método `__init__` para nuestra clase. Este método nos permite crear objetos `Stock` pasando los valores de los atributos `name`, `shares` y `price`.

3. Después de agregar el código, guarda el archivo. Esto asegurará que tus cambios se guarden y se puedan usar cuando ejecutes las pruebas.

4. Ahora, ejecutemos las pruebas para verificar tu implementación. Primero, cambia el directorio al directorio `~/project` ejecutando el siguiente comando:

```bash
cd ~/project
```

Luego, ejecuta las pruebas utilizando el siguiente comando:

```bash
python3 teststock.py
```

Si tu implementación es correcta, deberías ver una salida similar a esta:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Esta salida significa que todas las pruebas están pasando. ¡Los descriptores están validando correctamente los tipos de cada atributo!

Intentemos crear un objeto `Stock` en el intérprete de Python. Primero, asegúrate de estar en el directorio `~/project`. Luego, ejecuta el siguiente comando:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Deberías ver la siguiente salida:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

¡Has implementado con éxito descriptores para la verificación de tipos! Ahora, mejoremos este código aún más.
