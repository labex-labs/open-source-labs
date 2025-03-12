# Reescribir la clase Stock

Ahora que tenemos una clase base `Structure` bien definida, es hora de reescribir nuestra clase `Stock`. Al utilizar esta clase base, podemos simplificar nuestro código y hacerlo más organizado. La clase `Structure` proporciona un conjunto de funcionalidades comunes que podemos reutilizar en nuestra clase `Stock`, lo cual es una gran ventaja para la mantenibilidad y legibilidad del código.

## Crear la nueva clase Stock

Comencemos creando un nuevo archivo llamado `stock.py`. Este archivo contendrá nuestra clase `Stock` reescrita. Aquí está el código que debes poner en el archivo `stock.py`:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        """
        Calculate the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares):
        """
        Sell a number of shares
        """
        self.shares -= nshares
```

Analicemos lo que hace esta nueva clase `Stock`:

1. Hereda de la clase `Structure`. Esto significa que la clase `Stock` puede utilizar todas las características proporcionadas por la clase `Structure`. Una de las ventajas es que no necesitamos escribir un método `__init__` nosotros mismos porque la clase `Structure` se encarga de la asignación de atributos automáticamente.
2. Definimos `_fields`, que es una tupla que especifica los atributos de la clase `Stock`. Estos atributos son `name`, `shares` y `price`.
3. Se define la propiedad `cost` para calcular el costo total de las acciones. Multiplica el número de `shares` por el `price`.
4. El método `sell` se utiliza para reducir el número de acciones. Cuando se llama a este método con un número de acciones a vender, resta ese número del número actual de acciones.

## Probar la nueva clase Stock

Para asegurarnos de que nuestra nueva clase `Stock` funcione como se espera, necesitamos crear un archivo de prueba. Creemos un archivo llamado `test_stock.py` con el siguiente código:

```python
# test_stock.py
from stock import Stock

# Create a stock
s = Stock('GOOG', 100, 490.1)

# Check the attributes
print(f"Stock: {s}")
print(f"Name: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost}")

# Sell some shares
print("\nSelling 20 shares...")
s.sell(20)
print(f"Shares after selling: {s.shares}")
print(f"Cost after selling: {s.cost}")

# Try to set an invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.prices = 500  # Invalid attribute (should be 'price')
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

En este archivo de prueba, primero importamos la clase `Stock` del archivo `stock.py`. Luego creamos una instancia de la clase `Stock` con el nombre 'GOOG', 100 acciones y un precio de 490.1. Imprimimos los atributos de la acción para verificar si se han establecido correctamente. Después, vendemos 20 acciones e imprimimos el nuevo número de acciones y el nuevo costo. Finalmente, intentamos establecer un atributo inválido `prices` (debería ser `price`). Si nuestra clase `Stock` funciona correctamente, debería generar un `AttributeError`.

Para ejecutar la prueba, abre tu terminal y escribe el siguiente comando:

```bash
python3 test_stock.py
```

La salida esperada es la siguiente:

```
Stock: Stock('GOOG', 100, 490.1)
Name: GOOG
Shares: 100
Price: 490.1
Cost: 49010.0

Selling 20 shares...
Shares after selling: 80
Cost after selling: 39208.0

Trying to set an invalid attribute:
Error correctly caught: No attribute prices
```

## Ejecutar pruebas unitarias

Si tienes pruebas unitarias de ejercicios anteriores, puedes ejecutarlas contra tu nueva implementación. En tu terminal, escribe el siguiente comando:

```bash
python3 teststock.py
```

Ten en cuenta que algunas pruebas pueden fallar. Esto puede deberse a que esperan comportamientos o métodos específicos que aún no hemos implementado. ¡No te preocupes! Continuaremos construyendo sobre esta base en ejercicios futuros.

## Revisión de nuestro progreso

Tomemos un momento para revisar lo que hemos logrado hasta ahora:

1. Creamos una clase base `Structure` reutilizable. Esta clase:

   - Maneja automáticamente la asignación de atributos, lo que nos ahorra escribir mucho código repetitivo.
   - Proporciona una buena representación en cadena, lo que facilita imprimir y depurar nuestros objetos.
   - Restringe los nombres de los atributos para prevenir errores, lo que hace nuestro código más robusto.

2. Reescribimos nuestra clase `Stock`. Ella:
   - Hereda de la clase `Structure` para reutilizar la funcionalidad común.
   - Solo define los campos y métodos específicos del dominio, lo que mantiene la clase enfocada y limpia.
   - Tiene un diseño claro y sencillo, lo que la hace fácil de entender y mantener.

Este enfoque tiene varios beneficios para nuestro código:

- Es más mantenible porque hay menos repetición. Si necesitamos cambiar algo en la funcionalidad común, solo necesitamos cambiarlo en la clase `Structure`.
- Es más robusto debido a la mejor comprobación de errores proporcionada por la clase `Structure`.
- Es más legible porque las responsabilidades de cada clase son claras.

En ejercicios futuros, continuaremos construyendo sobre esta base para crear un sistema de gestión de carteras de acciones más sofisticado.
