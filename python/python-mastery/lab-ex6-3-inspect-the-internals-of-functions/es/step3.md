# Aplicando la inspección de funciones en clases

Ahora, vamos a tomar lo que hemos aprendido sobre la inspección de funciones y usarlo para mejorar la implementación de una clase. La inspección de funciones nos permite examinar el interior de las funciones y entender su estructura, como los parámetros que toman. En este caso, lo usaremos para hacer que nuestro código de clase sea más eficiente y menos propenso a errores. Modificaremos una clase `Structure` para que pueda detectar automáticamente los nombres de los campos a partir de la firma del método `__init__`.

## Entendiendo la clase `Structure`

El archivo `structure.py` contiene una clase `Structure`. Esta clase actúa como una clase base, lo que significa que otras clases pueden heredar de ella para crear objetos de datos estructurados. Actualmente, para definir los atributos de los objetos creados a partir de clases que heredan de `Structure`, necesitamos establecer una variable de clase `_fields`.

Abriremos el archivo en el editor. Usaremos el siguiente comando para navegar al directorio del proyecto:

```bash
cd ~/project
```

Una vez que hayas ejecutado este comando, puedes encontrar y ver la clase `Structure` existente en el archivo `structure.py` dentro del WebIDE.

## Creando una clase `Stock`

Vamos a crear una clase `Stock` que herede de la clase `Structure`. La herencia significa que la clase `Stock` obtendrá todas las características de la clase `Structure` y también puede agregar las suyas propias. Agregaremos el siguiente código al final del archivo `structure.py`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

Sin embargo, hay un problema con este enfoque. Tenemos que definir tanto la tupla `_fields` como el método `__init__` con los mismos nombres de parámetros. Esto es redundante porque esencialmente estamos escribiendo la misma información dos veces. Si olvidamos actualizar una cuando cambiamos la otra, puede causar errores.

## Agregando un método de clase `set_fields`

Para solucionar este problema, agregaremos un método de clase `set_fields` a la clase `Structure`. Este método detectará automáticamente los nombres de los campos a partir de la firma de `__init__`. Aquí está el código que necesitamos agregar a la clase `Structure`:

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

Este método utiliza el módulo `inspect`, que es una herramienta poderosa en Python para obtener información sobre objetos como funciones y clases. Primero, obtiene la firma del método `__init__`. Luego, extrae los nombres de los parámetros, pero omite el parámetro `self` porque `self` es un parámetro especial en las clases de Python que se refiere a la instancia misma. Finalmente, establece la variable de clase `_fields` con estos nombres de parámetros.

## Modificando la clase `Stock`

Ahora que tenemos el método `set_fields`, podemos simplificar nuestra clase `Stock`. Reemplaza el código anterior de la clase `Stock` con lo siguiente:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

De esta manera, no tenemos que definir manualmente la tupla `_fields`. El método `set_fields` se encargará de ello por nosotros.

## Probando la clase modificada

Para asegurarnos de que nuestra clase modificada funcione correctamente, crearemos un script de prueba simple. Crea un nuevo archivo llamado `test_structure.py` y agrega el siguiente código:

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

Este script de prueba crea un objeto `Stock`, prueba su representación como cadena, accede a sus atributos, modifica un atributo y trata de acceder a un atributo mal escrito para verificar si genera el error correcto.

Para ejecutar el script de prueba, usa el siguiente comando:

```bash
python3 test_structure.py
```

Deberías ver una salida similar a esta:

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## Cómo funciona

1. El método `set_fields` utiliza `inspect.signature()` para obtener los nombres de los parámetros del método `__init__`. Esta función nos da información detallada sobre los parámetros del método `__init__`.
2. Luego, establece automáticamente la variable de clase `_fields` en función de estos nombres de parámetros. Así, no tenemos que escribir los mismos nombres de parámetros en dos lugares diferentes.
3. Esto elimina la necesidad de definir manualmente tanto `_fields` como `__init__` con nombres de parámetros coincidentes. Hace que nuestro código sea más mantenible porque si cambiamos los parámetros en el método `__init__`, `_fields` se actualizará automáticamente.

Este enfoque utiliza la inspección de funciones para hacer que nuestro código sea más mantenible y menos propenso a errores. Es una aplicación práctica de las capacidades de introspección de Python, que nos permiten examinar y modificar objetos en tiempo de ejecución.
