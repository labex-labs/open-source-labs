# Creando un método **init**() dinámico

Ahora, vamos a aplicar lo que hemos aprendido sobre la función `exec()` a un escenario de programación del mundo real. En Python, la función `exec()` te permite ejecutar código Python almacenado en una cadena. En este paso, modificaremos la clase `Structure` para crear dinámicamente un método `__init__()`. El método `__init__()` es un método especial en las clases de Python, que se llama cuando se instancia un objeto de la clase. Basaremos la creación de este método en la variable de clase `_fields`, que contiene una lista de nombres de campos para la clase.

Primero, echemos un vistazo al archivo `structure.py` existente. Este archivo contiene la implementación actual de la clase `Structure` y una clase `Stock` que hereda de ella. Para ver el contenido del archivo, ábrelo en el WebIDE usando el siguiente comando:

```bash
cat /home/labex/project/structure.py
```

En la salida, verás que la implementación actual utiliza un enfoque manual para manejar la inicialización de objetos. Esto significa que el código para inicializar los atributos del objeto se escribe explícitamente, en lugar de ser generado dinámicamente.

Ahora, vamos a modificar la clase `Structure`. Agregaremos un método de clase `create_init()` que generará dinámicamente el método `__init__()`. Para hacer estos cambios, ábre el archivo `structure.py` en el editor del WebIDE y sigue estos pasos:

1. Elimina los métodos `_init()` y `set_fields()` existentes de la clase `Structure`. Estos métodos son parte del enfoque de inicialización manual, y no los necesitaremos más ya que vamos a usar un enfoque dinámico.

2. Agrega el método de clase `create_init()` a la clase `Structure`. Aquí está el código del método:

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

En este método, primero creamos una cadena `argstr` que contiene todos los nombres de campo separados por comas. Esta cadena se usará como la lista de argumentos para el método `__init__()`. Luego, creamos el código para el método `__init__()` como una cadena. Recorremos los nombres de campo y agregamos líneas al código que asignan cada argumento al atributo correspondiente del objeto. Después, usamos la función `exec()` para ejecutar el código y almacenar la función generada en el diccionario `locs`. Finalmente, usamos la función `setattr()` para establecer la función generada como el método `__init__()` de la clase.

3. Modifica la clase `Stock` para usar este nuevo enfoque:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Aquí, definimos los `_fields` para la clase `Stock` y luego llamamos al método `create_init()` para generar el método `__init__()` para la clase `Stock`.

Tu archivo `structure.py` completo ahora debería verse algo así:

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Ahora, probemos nuestra implementación para asegurarnos de que funcione correctamente. Ejecutaremos el archivo de pruebas unitarias para verificar si todas las pruebas pasan. Usa los siguientes comandos:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

Si tu implementación es correcta, deberías ver que todas las pruebas pasan. Esto significa que el método `__init__()` generado dinámicamente está funcionando como se espera.

También puedes probar la clase manualmente en la shell de Python. Así es como puedes hacerlo:

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

En la shell de Python, primero importamos la clase `Stock` del archivo `structure.py`. Luego, creamos una instancia de la clase `Stock` y la imprimimos. También podemos modificar el atributo `shares` del objeto. Sin embargo, cuando intentamos establecer un atributo que no existe en la lista `_fields`, deberíamos obtener un `AttributeError`.

¡Felicidades! Has utilizado con éxito la función `exec()` para crear dinámicamente un método `__init__()` basado en atributos de clase. Este enfoque puede hacer que tu código sea más flexible y fácil de mantener, especialmente cuando se trata de clases que tienen un número variable de atributos.
