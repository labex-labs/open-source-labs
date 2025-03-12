# Implementar el registro de eventos (logging)

En este paso, vamos a mejorar tu código. En lugar de usar simples mensajes de impresión (`print`), utilizaremos el módulo `logging` de Python para un adecuado registro de eventos. El registro de eventos es una excelente manera de llevar un seguimiento de lo que está haciendo tu programa, especialmente cuando se trata de manejar errores y entender el flujo de tu código.

## Comprender el módulo de registro de eventos

El módulo `logging` en Python nos proporciona una forma flexible de enviar mensajes de registro desde nuestras aplicaciones. Es mucho más poderoso que simplemente usar declaraciones de impresión simples. Esto es lo que puede hacer:

1. Diferentes niveles de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL): Estos niveles nos ayudan a categorizar la importancia de los mensajes. Por ejemplo, DEBUG es para información detallada que es útil durante el desarrollo, mientras que CRITICAL es para errores graves que pueden detener el programa.
2. Formato de salida configurable: Podemos decidir cómo se verán los mensajes de registro, como agregar marcas de tiempo u otra información útil.
3. Los mensajes se pueden dirigir a diferentes salidas (consola, archivos, etc.): Podemos elegir mostrar los mensajes de registro en la consola, guardarlos en un archivo o incluso enviarlos a un servidor remoto.
4. Filtrado de registros basado en la gravedad: Podemos controlar qué mensajes vemos en función de su nivel de registro.

## Agregar registro de eventos a reader.py

Ahora, cambiemos tu código para usar el módulo de registro de eventos. Abre el archivo `reader.py`.

Primero, necesitamos importar el módulo `logging` y configurar un registrador (logger) para este módulo. Agrega el siguiente código en la parte superior del archivo:

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

La declaración `import logging` importa el módulo `logging` para que podamos usar sus funciones. `logging.getLogger(__name__)` crea un registrador para este módulo específico. Usar `__name__` asegura que el registrador tenga un nombre único relacionado con el módulo.

A continuación, modificaremos la función `convert_csv()` para usar el registro de eventos en lugar de declaraciones de impresión. Aquí está el código actualizado:

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
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

Los cambios principales aquí son:

- Reemplazamos `print()` con `logger.warning()` para el mensaje de error. De esta manera, el mensaje se registra con el nivel de advertencia adecuado, y podemos controlar su visibilidad más adelante.
- Agregamos un nuevo mensaje `logger.debug()` con detalles sobre la excepción. Esto nos da más información sobre lo que salió mal, pero solo se muestra si el nivel de registro se establece en DEBUG o inferior.
- `str(e)` convierte la excepción en una cadena, para que podamos mostrar la razón del error en el mensaje de registro.

Después de realizar estos cambios, guarda el archivo.

## Probar el registro de eventos

Probemos tu código con el registro de eventos habilitado. Abre el intérprete de Python ejecutando el siguiente comando en tu terminal:

```bash
python3
```

Una vez que estés en el intérprete de Python, ejecuta el siguiente código:

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Aquí, primero importamos el módulo `logging` y nuestro módulo `reader`. Luego, establecemos el nivel de registro en DEBUG usando `logging.basicConfig(level=logging.DEBUG)`. Esto significa que veremos todos los mensajes de registro, incluyendo DEBUG, INFO, WARNING, ERROR y CRITICAL. Luego llamamos a la función `read_csv_as_dicts` del módulo `reader` e imprimimos el número de filas válidas procesadas.

Deberías ver una salida como esta:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Observa que el módulo de registro de eventos agrega un prefijo a cada mensaje, mostrando el nivel de registro (WARNING/DEBUG) y el nombre del módulo.

Ahora, veamos qué sucede si cambiamos el nivel de registro para mostrar solo las advertencias. Ejecuta el siguiente código en el intérprete de Python:

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Esta vez, establecemos el nivel de registro en WARNING usando `logging.basicConfig(level=logging.WARNING)`. Ahora solo verás los mensajes de WARNING, y los mensajes de DEBUG estarán ocultos:

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

Esto muestra la ventaja de usar diferentes niveles de registro. Podemos controlar cuántos detalles se muestran en los registros sin cambiar nuestro código.

Para salir del intérprete de Python, ejecuta el siguiente comando:

```python
exit()
```

¡Felicidades! Ahora has implementado un adecuado manejo de excepciones y registro de eventos en tu programa de Python. Esto hace que tu código sea más confiable y te brinda mejor información cuando se producen errores.
