# Explorando la inspección de marcos de pila (stack frames)

El enfoque `_init(locals())` que hemos estado utilizando es funcional, pero tiene un inconveniente. Cada vez que definimos un método `__init__`, tenemos que llamar explícitamente a `locals()`. Esto puede volverse un poco tedioso, especialmente cuando se trabajan con múltiples clases. Afortunadamente, podemos hacer que nuestro código sea más limpio y eficiente utilizando la inspección de marcos de pila. Esta técnica nos permite acceder automáticamente a las variables locales del llamador sin tener que llamar explícitamente a `locals()`.

Comencemos a explorar esta técnica en el intérprete de Python. Primero, abre tu terminal y navega al directorio del proyecto. Luego, inicia el intérprete de Python. Puedes hacer esto ejecutando los siguientes comandos:

```bash
cd ~/project
python3
```

Ahora que estamos en el intérprete de Python, necesitamos importar el módulo `sys`. El módulo `sys` proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python. Lo usaremos para acceder a la información del marco de pila.

```python
import sys
```

A continuación, definiremos una versión mejorada de nuestra función `_init()`. Esta nueva versión accederá directamente al marco del llamador, eliminando la necesidad de pasar `locals()` explícitamente.

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

En este código, `sys._getframe(1)` recupera el objeto de marco de la función llamadora. El `1` como argumento significa que estamos buscando un nivel más arriba en la pila de llamadas. Una vez que tenemos el objeto de marco, podemos acceder a sus variables locales utilizando `frame.f_locals`. Esto nos da un diccionario de todas las variables locales en el ámbito del llamador. Luego extraemos la variable `self` y establecemos las variables restantes como atributos del objeto `self`.

Ahora, probemos esta nueva función `_init()` con una nueva versión de nuestra clase `Stock`.

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

Como puedes ver, el método `__init__` ya no necesita pasar `locals()` explícitamente. Esto hace que nuestro código sea más limpio y fácil de leer desde la perspectiva del llamador.

### Cómo funciona la inspección de marcos de pila

Cuando llamas a `sys._getframe(1)`, Python devuelve el objeto de marco que representa el marco de ejecución del llamador. El argumento `1` significa "un nivel más arriba del marco actual" (la función llamadora).

Un objeto de marco contiene información importante sobre el contexto de ejecución. Esto incluye la función actual que se está ejecutando, las variables locales en esa función y el número de línea que se está ejecutando actualmente.

Al acceder a `frame.f_locals`, obtenemos un diccionario de todas las variables locales en el ámbito del llamador. Esto es similar a lo que `locals()` devolvería si se llamara directamente desde ese ámbito.

Esta técnica es bastante poderosa, pero debe usarse con cautela. Generalmente se considera una característica avanzada de Python y puede parecer un poco "mágica" porque se sale de los límites normales de ámbito de Python.

Una vez que hayas terminado de experimentar con la inspección de marcos de pila, puedes salir del intérprete de Python ejecutando el siguiente comando:

```python
exit()
```
