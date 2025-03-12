# Comprender las clases de validación

En este laboratorio, vamos a construir sobre un conjunto de clases de validación para crear un objeto invocable (callable object). Antes de comenzar a construir, es importante entender las clases de validación proporcionadas en el archivo `validate.py`. Estas clases nos ayudarán a realizar comprobaciones de tipo, que es una parte crucial para garantizar que nuestro código funcione como se espera.

Comencemos abriendo el archivo `validate.py` en el WebIDE. Este archivo contiene el código de las clases de validación que utilizaremos. Para abrirlo, ejecuta el siguiente comando en la terminal:

```bash
code /home/labex/project/validate.py
```

Una vez que hayas abierto el archivo, verás que contiene varias clases. Aquí está un breve resumen de lo que hace cada clase:

1. `Validator`: Esta es una clase base. Tiene un método `check`, pero actualmente este método no hace nada. Sirve como punto de partida para las otras clases de validación.
2. `Typed`: Esta es una subclase de `Validator`. Su función principal es comprobar si un valor es de un tipo específico.
3. `Integer`, `Float` y `String`: Estas son validadores de tipo específicos que heredan de `Typed`. Están diseñados para comprobar si un valor es un entero, un número de punto flotante o una cadena de texto, respectivamente.

Ahora, veamos cómo funcionan estas clases de validación en la práctica. Crearemos un nuevo archivo llamado `test.py` para probarlas. Para crear y abrir este archivo, ejecuta el siguiente comando:

```bash
code /home/labex/project/test.py
```

Una vez que el archivo `test.py` esté abierto, agrega el siguiente código a él. Este código probará los validadores `Integer` y `String`:

```python
from validate import Integer, String, Float

# Test Integer validator
print("Testing Integer validator:")
try:
    Integer.check(42)
    print("✓ Integer check passed for 42")
except TypeError as e:
    print(f"✗ Error: {e}")

try:
    Integer.check("Hello")
    print("✗ Integer check incorrectly passed for 'Hello'")
except TypeError as e:
    print(f"✓ Correctly raised error: {e}")

# Test String validator
print("\nTesting String validator:")
try:
    String.check("Hello")
    print("✓ String check passed for 'Hello'")
except TypeError as e:
    print(f"✗ Error: {e}")
```

En este código, primero importamos los validadores `Integer`, `String` y `Float` del archivo `validate.py`. Luego, probamos el validador `Integer` intentando comprobar un valor entero (`42`) y un valor de cadena (`"Hello"`). Si la comprobación pasa para el entero, imprimimos un mensaje de éxito. Si pasa incorrectamente para la cadena, imprimimos un mensaje de error. Si la comprobación levanta correctamente un `TypeError` para la cadena, imprimimos un mensaje de éxito. Hacemos una prueba similar para el validador `String`.

Después de agregar el código, ejecuta el archivo de prueba utilizando el siguiente comando:

```bash
python3 /home/labex/project/test.py
```

Deberías ver una salida similar a esta:

```
Testing Integer validator:
✓ Integer check passed for 42
✓ Correctly raised error: Expected <class 'int'>

Testing String validator:
✓ String check passed for 'Hello'
```

Como puedes ver, estas clases de validación nos permiten realizar comprobaciones de tipo fácilmente. Por ejemplo, cuando llamas a `Integer.check(x)`, levantará un `TypeError` si `x` no es un entero.

Ahora, pensemos en un escenario práctico. Supongamos que tenemos una función que requiere que sus argumentos sean de tipos específicos. Aquí hay un ejemplo de tal función:

```python
def add(x, y):
    Integer.check(x)  # Make sure x is an integer
    Integer.check(y)  # Make sure y is an integer
    return x + y
```

Esta función funciona, pero hay un problema. Tenemos que agregar manualmente las comprobaciones de validación cada vez que queremos usar la comprobación de tipo. Esto puede ser tedioso y propenso a errores, especialmente para funciones o proyectos más grandes.

En los siguientes pasos, resolveremos este problema creando un objeto invocable. Este objeto será capaz de aplicar automáticamente estas comprobaciones de tipo basadas en las anotaciones de la función. De esta manera, no tendremos que agregar las comprobaciones manualmente cada vez.
