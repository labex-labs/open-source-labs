# Clausuras como una Estructura de Datos

En Python, las clausuras (closures) ofrecen una forma poderosa de encapsular datos. El encapsulamiento significa mantener los datos privados y controlar el acceso a ellos. Con las clausuras, puedes crear funciones que administren y modifiquen datos privados sin tener que usar clases o variables globales. Las variables globales se pueden acceder y modificar desde cualquier parte de tu código, lo que puede llevar a un comportamiento inesperado. Las clases, por otro lado, requieren una estructura más compleja. Las clausuras proporcionan una alternativa más simple para el encapsulamiento de datos.

Vamos a crear un archivo llamado `counter.py` para demostrar este concepto:

1. Abre el WebIDE y crea un nuevo archivo llamado `counter.py` en el directorio `/home/labex/project`. Aquí es donde escribiremos el código que define nuestro contador basado en clausuras.

2. Agrega el siguiente código al archivo:

```python
def counter(value):
    """
    Create a counter with increment and decrement functions.

    Args:
        value: Initial value of the counter

    Returns:
        Two functions: one to increment the counter, one to decrement it
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

En este código, definimos una función llamada `counter()`. Esta función toma un `valor` inicial como argumento. Dentro de la función `counter()`, definimos dos funciones internas: `incr()` y `decr()`. Estas funciones internas comparten el acceso a la misma variable `valor`. La palabra clave `nonlocal` se utiliza para decirle a Python que queremos modificar la variable `valor` del ámbito envolvente (la función `counter()`). Sin la palabra clave `nonlocal`, Python crearía una nueva variable local dentro de las funciones internas en lugar de modificar el `valor` del ámbito externo.

3. Ahora, vamos a crear un archivo de prueba para ver esto en acción. Crea un nuevo archivo llamado `test_counter.py` con el siguiente contenido:

```python
from counter import counter

# Create a counter starting at 0
up, down = counter(0)

# Increment the counter several times
print("Incrementing the counter:")
print(up())  # Should print 1
print(up())  # Should print 2
print(up())  # Should print 3

# Decrement the counter
print("\nDecrementing the counter:")
print(down())  # Should print 2
print(down())  # Should print 1
```

En este archivo de prueba, primero importamos la función `counter()` del archivo `counter.py`. Luego, creamos un contador que comienza en 0 llamando a `counter(0)` y desempaquetando las funciones devueltas en `up` y `down`. Luego llamamos a la función `up()` varias veces para incrementar el contador e imprimimos los resultados. Después de eso, llamamos a la función `down()` para decrementar el contador e imprimimos los resultados.

4. Ejecuta el archivo de prueba ejecutando el siguiente comando en la terminal:

```bash
python3 test_counter.py
```

Deberías ver la siguiente salida:

```
Incrementing the counter:
1
2
3

Decrementing the counter:
2
1
```

Observa cómo aquí no está involucrada ninguna definición de clase. Las funciones `up()` y `down()` están manipulando un valor compartido que no es una variable global ni un atributo de instancia. Este valor se almacena en la clausura, lo que lo hace accesible solo para las funciones devueltas por `counter()`.

Este es un ejemplo de cómo las clausuras se pueden usar como una estructura de datos. La variable encerrada `valor` se mantiene entre llamadas a funciones y es privada para las funciones que la acceden. Esto significa que ninguna otra parte de tu código puede acceder o modificar directamente esta variable `valor`, lo que proporciona un nivel de protección de datos.
