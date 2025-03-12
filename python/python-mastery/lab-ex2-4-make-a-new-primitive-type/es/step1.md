# Creación de una clase MutInt básica

Comencemos creando una clase básica para nuestro tipo de entero mutable. En programación, una clase es como un plano para crear objetos. En este paso, crearemos la base de nuestro nuevo tipo primitivo. Un tipo primitivo es un tipo de dato básico proporcionado por un lenguaje de programación, y aquí vamos a construir el nuestro propio personalizado.

1. Abre el WebIDE y navega hasta el directorio `/home/labex/project`. El WebIDE es un entorno de desarrollo integrado donde puedes escribir, editar y ejecutar tu código. Navegar a este directorio asegura que todos tus archivos estén organizados en un solo lugar y puedan interactuar correctamente entre sí.

2. Abre el archivo `mutint.py` que se creó para ti en el paso de configuración. Este archivo será el lugar donde definiremos nuestra clase `MutInt`.

3. Añade el siguiente código para definir una clase `MutInt` básica:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value
```

El atributo `__slots__` se utiliza para definir los atributos que esta clase puede tener. Los atributos son como variables que pertenecen a un objeto de la clase. Al usar `__slots__`, le decimos a Python que utilice una forma más eficiente en memoria para almacenar los atributos. En este caso, nuestra clase `MutInt` solo tendrá un único atributo llamado `value`. Esto significa que cada objeto de la clase `MutInt` solo podrá contener un dato, que es el valor entero.

El método `__init__` es el constructor de nuestra clase. Un constructor es un método especial que se llama cuando se crea un objeto de la clase. Toma un parámetro `value` y lo almacena en el atributo `value` de la instancia. Una instancia es un objeto individual creado a partir del plano de la clase.

Vamos a probar nuestra clase creando un script de Python para usarla:

4. Crea un nuevo archivo llamado `test_mutint.py` en el mismo directorio:

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

En este script de prueba, primero importamos la clase `MutInt` del archivo `mutint.py`. Luego creamos un objeto de la clase `MutInt` con un valor inicial de 3. Imprimimos el valor inicial, luego lo modificamos a 42 e imprimimos el nuevo valor. Finalmente, intentamos sumar 10 al objeto `MutInt`, lo que resultará en un error porque nuestra clase aún no admite la operación de suma.

5. Ejecuta el script de prueba ejecutando el siguiente comando en la terminal:

```bash
python3 /home/labex/project/test_mutint.py
```

La terminal es una interfaz de línea de comandos donde puedes ejecutar varios comandos para interactuar con tu sistema y tu código. Ejecutar este comando ejecutará el script `test_mutint.py`.

Deberías ver una salida similar a esta:

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

Nuestra clase `MutInt` almacena y actualiza un valor correctamente. Sin embargo, tiene varias limitaciones:

- No se muestra correctamente cuando se imprime.
- No admite operaciones matemáticas como la suma.
- No admite comparaciones.
- No admite conversiones de tipo.

En los siguientes pasos, abordaremos estas limitaciones una por una para hacer que nuestra clase `MutInt` se comporte más como un verdadero tipo primitivo.
