# Ejecución de función retrasada

## Problema

Escribe una función `delay(fn, ms, *args)` que tome una función `fn`, un tiempo en milisegundos `ms` y cualquier número de argumentos `args`. La función debe retrasar la ejecución de `fn` durante `ms` milisegundos y luego invocarla con los argumentos proporcionados. La función debe devolver el resultado de invocar `fn`.

Para retrasar la ejecución de `fn`, utiliza la función `time.sleep()`. Esta función toma un número de segundos como argumento, por lo que necesitarás convertir `ms` a segundos antes de pasarlo a `time.sleep()`.

## Ejemplo

```python
def add(x, y):
  return x + y

result = delay(add, 2000, 2, 3)
print(result) # Output: 5
```

En el ejemplo anterior, la función `add` se retrasa 2000 milisegundos (2 segundos) antes de ser invocada con los argumentos `2` y `3`. Luego se devuelve el resultado de la función `add` y se imprime en la consola.
