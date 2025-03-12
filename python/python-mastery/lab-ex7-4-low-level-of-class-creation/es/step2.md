# Creación de un ayudante para estructuras tipadas

En este paso, vamos a construir un ejemplo más práctico. Implementaremos una función que crea clases con validación de tipos. La validación de tipos es crucial ya que asegura que los datos asignados a los atributos de la clase cumplan con criterios específicos, como ser de un cierto tipo de dato o estar dentro de un rango particular. Esto ayuda a detectar errores temprano y hace que nuestro código sea más robusto.

## Comprender la clase Structure

Primero, necesitamos abrir el archivo `structure.py` en el editor de WebIDE. Este archivo contiene una clase `Structure` básica. Esta clase proporciona la funcionalidad fundamental para inicializar y representar objetos estructurados. La inicialización significa configurar el objeto con los datos proporcionados, y la representación se refiere a cómo se muestra el objeto cuando lo imprimimos.

Para abrir el archivo, usaremos el siguiente comando en la terminal:

```bash
cd ~/project
```

Después de ejecutar este comando, estarás en el directorio correcto donde se encuentra el archivo `structure.py`. Cuando abras el archivo, notarás la clase `Structure` básica. Nuestro objetivo es extender esta clase para que admita la validación de tipos.

## Implementar la función typed_structure

Ahora, agreguemos la función `typed_structure` al archivo `structure.py`. Esta función creará una nueva clase que herede de la clase `Structure` e incluya los validadores especificados. La herencia significa que la nueva clase tendrá toda la funcionalidad de la clase `Structure` y también puede agregar sus propias características. Los validadores se utilizan para comprobar si los valores asignados a los atributos de la clase son válidos.

Aquí está el código para la función `typed_structure`:

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

El parámetro `clsname` es el nombre que queremos dar a la nueva clase. El parámetro `validators` es un diccionario donde las claves son los nombres de los atributos y los valores son los objetos validador. La función `type()` se utiliza para crear una nueva clase de forma dinámica. Toma tres argumentos: el nombre de la clase, una tupla de clases base (en este caso, solo la clase `Structure`) y un diccionario de atributos de clase (los validadores).

Después de agregar esta función, tu archivo `structure.py` debería verse así:

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Probar la función typed_structure

Probemos nuestra función `typed_structure` utilizando los validadores del archivo `validate.py`. Estos validadores se utilizan para comprobar si los valores asignados a los atributos de la clase son del tipo correcto y cumplen con otros criterios.

Primero, abre una shell interactiva de Python. Usaremos los siguientes comandos en la terminal:

```bash
cd ~/project
python3
```

El primer comando nos lleva al directorio correcto, y el segundo comando inicia la shell interactiva de Python.

Ahora, importa los componentes necesarios y crea una estructura tipada:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

Importamos los validadores `String`, `PositiveInteger` y `PositiveFloat` del archivo `validate.py`. Luego usamos la función `typed_structure` para crear una clase `Stock` con validación de tipos. Creamos una instancia de la clase `Stock` y la probamos imprimiendo sus atributos. Finalmente, intentamos crear una instancia de acción no válida para probar la validación.

Deberías ver una salida similar a:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

Cuando termines de probar, sal de la shell de Python:

```python
exit()
```

Este ejemplo demuestra cómo podemos usar la función `type()` para crear clases personalizadas con reglas de validación específicas. Este enfoque es muy poderoso ya que nos permite generar clases de forma programática, lo que puede ahorrar mucho tiempo y hacer que nuestro código sea más flexible.
