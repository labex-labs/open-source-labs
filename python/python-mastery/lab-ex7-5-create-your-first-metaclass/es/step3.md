# Usando tu Metaclase

Ahora, vamos a crear una clase que utilice nuestra metaclase a través de la herencia. Esto nos ayudará a entender cómo se llama la metaclase cuando se define la clase.

Una metaclase en Python es una clase que crea otras clases. Cuando defines una clase, Python utiliza una metaclase para construir ese objeto de clase. Al utilizar la herencia, podemos especificar qué metaclase debe utilizar una clase.

1. Abre `mymeta.py` y agrega el siguiente código al final del archivo:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Aquí, estamos definiendo una clase `Stock` que hereda de `myobject`. El método `__init__` es un método especial en las clases de Python. Se llama cuando se crea un objeto de la clase y se utiliza para inicializar los atributos del objeto. El método `cost` calcula el costo total de las acciones, y el método `sell` reduce el número de acciones.

2. Guarda el archivo presionando Ctrl+S. Guardar el archivo asegura que los cambios que has realizado se almacenen y se puedan ejecutar más tarde.

3. Ahora, ejecutemos el archivo para ver qué sucede. Abre una terminal en el WebIDE y ejecuta:

```bash
cd /home/labex/project
python3 mymeta.py
```

El comando `cd` cambia el directorio de trabajo actual a `/home/labex/project`, y `python3 mymeta.py` ejecuta el script de Python `mymeta.py`.

Deberías ver una salida similar a esta:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

Esta salida muestra que nuestra metaclase se está invocando cuando se crean tanto la clase `myobject` como la clase `Stock`. Observa cómo:

- Para `Stock`, las clases base incluyen `myobject` porque `Stock` hereda de `myobject`.
- La lista de atributos incluye todos los métodos que definimos (`__init__`, `cost`, `sell`) junto con algunos atributos predeterminados.

4. Interactuemos con nuestra clase `Stock`. Crea un nuevo archivo llamado `test_stock.py` con el siguiente contenido:

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

En este código, estamos importando la clase `Stock` del módulo `mymeta`. Luego creamos una instancia de la clase `Stock` llamada `apple`. Utilizamos los métodos de la clase `Stock` para imprimir información sobre las acciones, calcular el costo total, vender algunas acciones y luego imprimir la información actualizada.

5. Ejecuta este archivo para probar nuestra clase `Stock`:

```bash
python3 test_stock.py
```

Deberías ver una salida como esta:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Observa que la información de nuestra metaclase se imprime primero, seguida de la salida de nuestro script de prueba. Esto se debe a que la metaclase se invoca cuando se define la clase, lo que ocurre antes de que se ejecute el código en el script de prueba.
