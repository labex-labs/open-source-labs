# Implementar el manejo de excepciones

En este paso, nos centraremos en hacer que tu código sea más robusto. Cuando un programa encuentra datos incorrectos, a menudo se bloquea. Pero podemos utilizar una técnica llamada manejo de excepciones para manejar estos problemas de manera elegante. Modificarás el archivo `reader.py` para implementar esto. El manejo de excepciones permite que tu programa siga ejecutándose incluso cuando se enfrenta a datos inesperados, en lugar de detenerse abruptamente.

## Comprender los bloques try-except

Python proporciona una forma poderosa de manejar excepciones utilizando bloques try-except. Analicemos cómo funcionan.

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

En el bloque `try`, colocas el código que podría generar una excepción. Una excepción es un error que ocurre durante la ejecución de un programa. Por ejemplo, si intentas dividir un número entre cero, Python generará una excepción `ZeroDivisionError`. Cuando se produce una excepción en el bloque `try`, Python detiene la ejecución del código en el bloque `try` y salta al bloque `except` correspondiente. El bloque `except` contiene el código que manejará la excepción. `SomeExceptionType` es el tipo de excepción que quieres capturar. Puedes capturar tipos específicos de excepciones o utilizar una excepción general `Exception` para capturar todos los tipos de excepciones. La parte `as e` te permite acceder al objeto de excepción, que contiene información sobre el error.

## Modificar el código

Ahora, apliquemos lo que hemos aprendido sobre los bloques try-except a la función `convert_csv()`. Abre el archivo `reader.py` en tu editor.

1. Reemplaza la función `convert_csv()` actual con el siguiente código:

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

En esta nueva implementación:

- Utilizamos un bucle `for` en lugar de `map()` para procesar cada fila. Esto nos da más control sobre el procesamiento de cada fila.
- Encerramos el código de conversión en un bloque try-except. Esto significa que si se produce una excepción durante la conversión de una fila, el programa no se bloqueará. En lugar de eso, saltará al bloque `except`.
- En el bloque `except`, imprimimos un mensaje de error para las filas no válidas. Esto nos ayuda a identificar qué filas tienen problemas.
- Después de imprimir el mensaje de error, utilizamos la declaración `continue` para omitir la fila actual y continuar procesando las filas restantes.

Guarda el archivo después de realizar estos cambios.

## Probar tus cambios

Probemos tu código modificado con el archivo `missing.csv`. Primero, abre el intérprete de Python ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Una vez que estés en el intérprete de Python, ejecuta el siguiente código:

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Cuando ejecutes este código, deberías ver mensajes de error para cada fila problemática. Pero el programa seguirá procesando y devolverá las filas válidas. Aquí tienes un ejemplo de lo que podrías ver:

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

Verifiquemos también que el programa funcione correctamente con datos válidos. Ejecuta el siguiente código en el intérprete de Python:

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

Deberías ver que todas las filas se procesan sin errores. Aquí tienes un ejemplo de la salida:

```
Number of valid rows processed: 17
```

Para salir del intérprete de Python, ejecuta el siguiente comando:

```python
exit()
```

Ahora tu código es más robusto. Puede manejar datos no válidos de manera elegante omitiendo las filas incorrectas en lugar de bloquearse. Esto hace que tu programa sea más confiable y amigable para el usuario.
