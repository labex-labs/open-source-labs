# Implementando la inicialización avanzada en la estructura

Acabamos de aprender dos técnicas poderosas para acceder a los argumentos de una función. Ahora, usaremos estas técnicas para actualizar nuestra clase `Structure`. Primero, entendamos por qué estamos haciendo esto. Estas técnicas harán que nuestra clase sea más flexible y fácil de usar, especialmente cuando se trate de diferentes tipos de argumentos.

Abre el archivo `structure.py` en el editor de código. Puedes hacer esto ejecutando los siguientes comandos en la terminal. El comando `cd` cambia el directorio al directorio del proyecto, y el comando `code` abre el archivo `structure.py` en el editor de código.

```bash
cd ~/project
code structure.py
```

Reemplaza el contenido del archivo con el siguiente código. Este código define una clase `Structure` con varios métodos. Analicemos cada parte para entender lo que hace.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Esto es lo que hemos hecho en el código:

1. Eliminamos el antiguo método `__init__()`. Dado que las subclases definirán sus propios métodos `__init__`, ya no necesitamos el antiguo.
2. Añadimos un nuevo método estático `_init()`. Este método utiliza la inspección de marcos para capturar y establecer automáticamente todos los parámetros como atributos. La inspección de marcos nos permite acceder a las variables locales del método llamador.
3. Mantenimos el método `__repr__()`. Este método proporciona una buena representación en cadena del objeto, lo cual es útil para la depuración y la impresión.
4. Añadimos un método `__setattr__()`. Este método aplica la validación de atributos, asegurando que solo se puedan establecer atributos válidos en el objeto.

Ahora, actualicemos la clase `Stock`. Abre el archivo `stock.py` utilizando el siguiente comando:

```bash
code stock.py
```

Reemplaza su contenido con el siguiente código:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

El cambio clave aquí es que nuestro método `__init__` ahora llama a `self._init()` en lugar de establecer manualmente cada atributo. El método `_init()` utiliza la inspección de marcos para capturar y establecer automáticamente todos los parámetros como atributos. Esto hace que el código sea más conciso y fácil de mantener.

Probemos nuestra implementación ejecutando las pruebas unitarias. Las pruebas unitarias nos ayudarán a asegurarnos de que nuestro código funciona como se espera. Ejecuta los siguientes comandos en la terminal:

```bash
cd ~/project
python3 teststock.py
```

Deberías ver que todas las pruebas pasan, incluyendo la prueba para argumentos de palabra clave que fallaba antes. Esto significa que nuestra implementación está funcionando correctamente.

Veamos también la documentación de ayuda para nuestra clase `Stock`. La documentación de ayuda proporciona información sobre la clase y sus métodos. Ejecuta el siguiente comando en la terminal:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Ahora deberías ver una firma adecuada para el método `__init__`, mostrando todos los nombres de los parámetros. Esto hace que sea más fácil para otros desarrolladores entender cómo usar la clase.

Finalmente, probemos de forma interactiva que los argumentos de palabra clave funcionan como se espera. Ejecuta el siguiente comando en la terminal:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Deberías ver que el objeto `Stock` se crea correctamente con los atributos especificados. Esto confirma que nuestro sistema de inicialización de clase admite argumentos de palabra clave.

Con esta implementación, hemos logrado un sistema de inicialización de clase mucho más flexible y fácil de usar que:

1. Preserva las firmas de función adecuadas en la documentación, lo que hace que sea más fácil para los desarrolladores entender cómo usar la clase.
2. Admite tanto argumentos posicionales como de palabra clave, proporcionando más flexibilidad al crear objetos.
3. Requiere un código de plantilla mínimo en las subclases, reduciendo la cantidad de código que debes escribir.
