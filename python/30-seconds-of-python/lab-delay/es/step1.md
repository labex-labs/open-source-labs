# Ejecución de función retrasada

Escribe una función `delay(fn, ms, *args)` que tome una función `fn`, un tiempo en milisegundos `ms` y cualquier número de argumentos `args`. La función debe retrasar la ejecución de `fn` durante `ms` milisegundos y luego invocarla con los argumentos proporcionados. La función debe devolver el resultado de invocar `fn`.

Para retrasar la ejecución de `fn`, utiliza la función `time.sleep()`. Esta función toma un número de segundos como argumento, por lo que necesitarás convertir `ms` a segundos antes de pasarlo a `time.sleep()`.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # imprime 'later' después de un segundo
```
