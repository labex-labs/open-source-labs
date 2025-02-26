# Tubos de Generador

Puedes utilizar este aspecto de los generadores para configurar tuberías de procesamiento (como las tuberías de Unix).

_productor_ → _procesamiento_ → _procesamiento_ → _consumidor_

Las tuberías de procesamiento tienen un productor de datos inicial, un conjunto de etapas de procesamiento intermedio y un consumidor final.

**productor** → _procesamiento_ → _procesamiento_ → _consumidor_

```python
def producer():
 ...
    yield item
 ...
```

El productor es típicamente un generador. Aunque también podría ser una lista u otra secuencia. `yield` alimenta datos a la tubería.

_productor_ → _procesamiento_ → _procesamiento_ → **consumidor**

```python
def consumer(s):
    for item in s:
 ...
```

El consumidor es un bucle `for`. Recibe los elementos y hace algo con ellos.

_productor_ → **procesamiento** → **procesamiento** → _consumidor_

```python
def processing(s):
    for item in s:
 ...
        yield newitem
 ...
```

Las etapas de procesamiento intermedio consumen y producen elementos al mismo tiempo. Pueden modificar el flujo de datos. También pueden filtrar (descartando elementos).

_productor_ → _procesamiento_ → _procesamiento_ → _consumidor_

```python
def producer():
 ...
    yield item          # produce el elemento que recibe el `procesamiento`
 ...

def processing(s):
    for item in s:      # Viene del `productor`
 ...
        yield newitem   # produce un nuevo elemento
 ...

def consumer(s):
    for item in s:      # Viene del `procesamiento`
 ...
```

Código para configurar la tubería

```python
a = producer()
b = processing(a)
c = consumer(b)
```

Notarás que los datos fluyen incrementalmente a través de las diferentes funciones.

Para este ejercicio, el programa `stocksim.py` debe seguir ejecutándose en segundo plano. Vas a utilizar la función `follow()` que escribiste en el ejercicio anterior.
