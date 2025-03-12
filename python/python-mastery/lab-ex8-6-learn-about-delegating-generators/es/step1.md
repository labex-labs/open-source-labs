# Comprender la declaración `yield from`

En este paso, vamos a explorar la declaración `yield from` en Python. Esta declaración es una herramienta poderosa cuando se trabaja con generadores, y simplifica el proceso de delegar operaciones a otros generadores. Al final de este paso, entenderás qué es `yield from`, cómo funciona y cómo puede manejar el paso de valores entre diferentes generadores.

## ¿Qué es `yield from`?

La declaración `yield from` se introdujo en Python 3.3. Su propósito principal es simplificar la delegación de operaciones a subgeneradores. Un subgenerador es simplemente otro generador al que un generador principal puede delegar trabajo.

Normalmente, cuando quieres que un generador devuelva valores de otro generador, tendrías que usar un bucle. Por ejemplo, sin `yield from`, escribirías código como este:

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

En este código, el `delegating_generator` utiliza un bucle `for` para iterar sobre los valores producidos por `subgenerator` y luego devuelve cada valor uno por uno.

Sin embargo, con la declaración `yield from`, el código se vuelve mucho más simple:

```python
def delegating_generator():
    yield from subgenerator()
```

Esta única línea de código logra el mismo resultado que el bucle en el ejemplo anterior. Pero `yield from` no es solo un atajo. También gestiona la comunicación bidireccional entre el llamador y el subgenerador. Esto significa que cualquier valor enviado al generador delegador se pasa directamente al subgenerador.

## Ejemplo básico

Vamos a crear un ejemplo simple para ver cómo funciona `yield from` en acción.

1. Primero, necesitamos abrir el archivo `cofollow.py` en el editor. Para hacer esto, usaremos el comando `cd` para navegar al directorio correcto. Ejecuta el siguiente comando en la terminal:

```bash
cd /home/labex/project
```

2. A continuación, agregaremos dos funciones al archivo `cofollow.py`. La función `subgen` es un generador simple que devuelve los números del 0 al 4. La función `main_gen` utiliza `yield from` para delegar la generación de estos números a `subgen` y luego devuelve la cadena `'Done'`. Agrega el siguiente código al final del archivo `cofollow.py`:

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. Ahora, vamos a probar estas funciones. Abre una shell de Python y ejecuta el siguiente código:

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

Cuando ejecutes este código, deberías ver la siguiente salida:

```
0
1
2
3
4

0
1
2
3
4
Done
```

Esta salida muestra que `yield from` permite que `main_gen` pase todos los valores generados por `subgen` directamente al llamador.

## Paso de valores con `yield from`

Una de las características más poderosas de `yield from` es su capacidad para manejar el paso de valores en ambas direcciones. Vamos a crear un ejemplo más complejo para demostrar esto.

1. Agrega las siguientes funciones al archivo `cofollow.py`:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

La función `accumulator` es una corutina que lleva la cuenta de un total acumulado. Devuelve el total actual y luego espera para recibir un nuevo valor. Si recibe `None`, detiene el bucle. La función `caller` crea una instancia de `accumulator` y utiliza `yield from` para delegar todas las operaciones de envío y recepción a ella.

2. Prueba estas funciones en una shell de Python:

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

Cuando ejecutes este código, deberías ver la siguiente salida:

```
0
1
3
6
'Total accumulated'
```

Esta salida muestra que `yield from` delega completamente todas las operaciones de envío y recepción al subgenerador hasta que se agota.

Ahora que entiendes los conceptos básicos de `yield from`, pasaremos a aplicaciones más prácticas en el siguiente paso.
