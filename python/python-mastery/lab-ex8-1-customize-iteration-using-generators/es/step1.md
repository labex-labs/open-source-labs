# Comprendiendo los generadores de Python

Los generadores son una característica poderosa en Python. Ofrecen una forma simple y elegante de crear iteradores. En Python, cuando se trabaja con secuencias de datos, los iteradores son muy útiles ya que permiten recorrer una serie de valores uno por uno. Las funciones regulares normalmente devuelven un solo valor y luego dejan de ejecutarse. Sin embargo, los generadores son diferentes. Pueden generar una secuencia de valores con el tiempo, lo que significa que pueden producir múltiples valores de forma gradual.

## ¿Qué es un generador?

Una función generadora tiene una apariencia similar a una función regular. Pero la diferencia clave radica en cómo devuelve valores. En lugar de usar la declaración `return` para proporcionar un solo resultado, una función generadora utiliza la declaración `yield`. La declaración `yield` es especial. Cada vez que se ejecuta, el estado de la función se pausa y el valor que sigue a la palabra clave `yield` se devuelve al llamador. Cuando se llama a la función generadora de nuevo, se reanuda la ejecución justo donde se dejó.

Comencemos creando una función generadora simple. La función incorporada `range()` en Python no admite pasos fraccionarios. Entonces, crearemos una función generadora que pueda producir un rango de números con un paso fraccionario.

1. Primero, debes abrir una nueva terminal de Python en el WebIDE. Para hacer esto, haz clic en el menú "Terminal" y luego selecciona "Nueva Terminal".
2. Una vez que la terminal esté abierta, escribe el siguiente código en la terminal. Este código define una función generadora y luego la prueba.

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

En este código, la función `frange` es una función generadora. Inicializa una variable `current` con el valor `start`. Luego, siempre que `current` sea menor que el valor `stop`, produce el valor `current` y luego incrementa `current` en el valor `step`. El bucle `for` luego itera sobre los valores producidos por la función generadora `frange` y los imprime.

Deberías ver la siguiente salida:

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## La naturaleza de un solo uso de los generadores

Una característica importante de los generadores es que son agotables. Esto significa que una vez que has iterado sobre todos los valores producidos por un generador, no se puede usar de nuevo para producir la misma secuencia de valores. Demostremos esto con el siguiente código:

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

En este código, primero creamos un objeto generador `f` utilizando la función `frange`. El primer bucle `for` itera sobre todos los valores producidos por el generador y los imprime. Después de la primera iteración, el generador se ha agotado, lo que significa que ya ha producido todos los valores que puede. Entonces, cuando intentamos iterar sobre él de nuevo en el segundo bucle `for`, no produce ningún valor nuevo.

Salida:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Observa que la segunda iteración no produjo ninguna salida porque el generador ya estaba agotado.

## Creando generadores reutilizables con clases

Si necesitas iterar varias veces sobre la misma secuencia de valores, puedes envolver el generador en una clase. Al hacer esto, cada vez que inicies una nueva iteración, se creará un nuevo generador.

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

En este código, definimos una clase `FRange`. El método `__init__` inicializa los valores `start`, `stop` y `step`. El método `__iter__` es un método especial en las clases de Python. Se utiliza para crear un iterador. Dentro del método `__iter__`, tenemos un generador que produce valores de manera similar a la función `frange` que definimos anteriormente.

Cuando creamos una instancia `f` de la clase `FRange` e iteramos sobre ella varias veces, cada iteración llama al método `__iter__`, que crea un nuevo generador. Entonces, podemos obtener la misma secuencia de valores varias veces.

Salida:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

Esta vez, podemos iterar varias veces porque el método `__iter__()` crea un nuevo generador cada vez que se llama.
