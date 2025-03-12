# Creación de objetos de solo lectura con proxies

En este paso, vamos a explorar las clases proxy, un patrón muy útil en Python. Las clases proxy te permiten tomar un objeto existente y cambiar su comportamiento sin alterar su código original. Esto es como poner una envoltura especial alrededor de un objeto para agregar nuevas características o restricciones.

## ¿Qué es un proxy?

Un proxy es un objeto que se interpone entre tú y otro objeto. Tiene el mismo conjunto de funciones y propiedades que el objeto original, pero puede hacer cosas adicionales. Por ejemplo, puede controlar quién puede acceder al objeto, mantener un registro de las acciones (registro de eventos o "logging"), o agregar otras características útiles.

Vamos a crear un proxy de solo lectura. Este tipo de proxy evitará que cambies los atributos de un objeto.

### Paso 1: Crear la clase proxy de solo lectura

Primero, necesitamos crear un archivo de Python que defina nuestro proxy de solo lectura.

1. Navega al directorio `/home/labex/project`.
2. Crea un nuevo archivo llamado `readonly_proxy.py` en este directorio.
3. Abre el archivo `readonly_proxy.py` y agrega el siguiente código:

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

En este código, se define la clase `ReadonlyProxy`. El método `__init__` almacena el objeto que queremos envolver. Usamos `self.__dict__` para almacenarlo directamente y evitar llamar al método `__setattr__`. El método `__getattr__` se utiliza cuando intentamos acceder a un atributo del proxy. Simplemente pasa la solicitud al objeto envuelto. El método `__setattr__` se llama cuando intentamos cambiar un atributo. Levanta un error para evitar cualquier cambio.

### Paso 2: Crear un archivo de prueba

Ahora, crearemos un archivo de prueba para ver cómo funciona nuestro proxy de solo lectura.

1. Crea un nuevo archivo llamado `test_readonly.py` en el mismo directorio `/home/labex/project`.
2. Agrega el siguiente código al archivo `test_readonly.py`:

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

En este código de prueba, primero creamos un objeto `Stock` normal e imprimimos su información. Luego modificamos uno de sus atributos e imprimimos la información actualizada. A continuación, creamos un proxy de solo lectura para el objeto `Stock` e imprimimos su información. Finalmente, intentamos modificar el proxy de solo lectura y esperamos obtener un error.

### Paso 3: Ejecutar el script de prueba

Después de crear la clase proxy y el archivo de prueba, necesitamos ejecutar el script de prueba para ver los resultados.

1. Abre una terminal y navega al directorio `/home/labex/project` usando el siguiente comando:

```bash
cd /home/labex/project
```

2. Ejecuta el script de prueba usando el siguiente comando:

```bash
python3 test_readonly.py
```

Deberías ver una salida similar a:

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## Cómo funciona el proxy

La clase `ReadonlyProxy` utiliza dos métodos especiales para lograr su funcionalidad de solo lectura:

1. `__getattr__(self, name)`: Este método se llama cuando Python no puede encontrar un atributo de la manera normal. En nuestra clase `ReadonlyProxy`, usamos la función `getattr()` para pasar la solicitud de acceso al atributo al objeto envuelto. Entonces, cuando intentas acceder a un atributo del proxy, en realidad obtendrás el atributo del objeto envuelto.

2. `__setattr__(self, name, value)`: Este método se llama cuando intentas asignar un valor a un atributo. En nuestra implementación, levantamos un `AttributeError` para evitar que se realicen cambios en los atributos del proxy.

3. En el método `__init__`, modificamos directamente `self.__dict__` para almacenar el objeto envuelto. Esto es importante porque si usáramos la forma normal de asignar el objeto, se llamaría al método `__setattr__`, que levantaría un error.

Este patrón de proxy nos permite agregar una capa de solo lectura alrededor de cualquier objeto existente sin cambiar su clase original. El objeto proxy se comporta como el objeto envuelto, pero no te permitirá realizar modificaciones.
