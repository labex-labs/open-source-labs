# Comprender las excepciones en Python

En este paso, vamos a aprender sobre las excepciones en Python. Las excepciones son un concepto importante en la programación. Nos ayudan a manejar situaciones inesperadas que pueden ocurrir mientras un programa está en ejecución. También descubriremos por qué el código actual se bloquea cuando intenta procesar datos no válidos. Comprender esto te ayudará a escribir programas de Python más robustos y confiables.

## ¿Qué son las excepciones?

En Python, las excepciones son eventos que ocurren durante la ejecución de un programa y interrumpen el flujo normal de las instrucciones. Piénsalo como un obstáculo en una carretera. Cuando todo va bien, tu programa sigue un camino establecido, al igual que un automóvil en una carretera despejada. Pero cuando ocurre un error, Python crea un objeto de excepción. Este objeto es como un informe que contiene información sobre lo que salió mal, como el tipo de error y dónde ocurrió en el código.

Si estas excepciones no se manejan adecuadamente, hacen que el programa se bloquee. Cuando se produce un bloqueo, Python muestra un mensaje de rastreo (traceback). Este mensaje es como un mapa que te muestra la ubicación exacta en el código donde ocurrió el error. Es muy útil para la depuración.

## Examinar el código actual

Primero, echemos un vistazo a la estructura del archivo `reader.py`. Este archivo contiene funciones que se utilizan para leer y convertir datos CSV. Para abrir el archivo en el editor, necesitamos navegar al directorio correcto. Usaremos el comando `cd` en la terminal.

```bash
cd /home/labex/project
```

Ahora que estamos en el directorio correcto, echemos un vistazo al contenido de `reader.py`. Este archivo tiene varias funciones importantes:

1. `convert_csv()`: Esta función toma filas de datos y utiliza una función de conversión proporcionada para convertirlas. Es como una máquina que toma materias primas (filas de datos) y las transforma en una forma diferente según una receta específica (la función de conversión).
2. `csv_as_dicts()`: Esta función lee datos CSV y los convierte en una lista de diccionarios. También realiza la conversión de tipos, lo que significa que se asegura de que cada pieza de datos en el diccionario sea del tipo correcto, como una cadena, un entero o un número de punto flotante.
3. `read_csv_as_dicts()`: Esta es una función envolvente (wrapper). Es como un gerente que llama a la función `csv_as_dicts()` para que se haga el trabajo.

## Demostrar el problema

Veamos qué sucede cuando el código intenta procesar datos no válidos. Abriremos un intérprete de Python, que es como un campo de juego donde podemos probar nuestro código de Python de forma interactiva. Para abrir el intérprete de Python, usaremos el siguiente comando en la terminal:

```bash
python3
```

Una vez que el intérprete de Python esté abierto, intentaremos leer el archivo `missing.csv`. Este archivo contiene algunos datos faltantes o no válidos. Usaremos la función `read_csv_as_dicts()` del archivo `reader.py` para leer los datos.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Cuando ejecutes este código, deberías ver un mensaje de error como este:

```
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: ''
```

Este error ocurre porque el código intenta convertir una cadena vacía en un entero. Una cadena vacía no representa un entero válido, por lo que Python no puede realizar la conversión. La función se bloquea en el primer error que encuentra y deja de procesar el resto de los datos válidos en el archivo.

Para salir del intérprete de Python, escribe el siguiente comando:

```python
exit()
```

## Comprender el flujo de errores

El error ocurre en la función `convert_csv()`, específicamente en la siguiente línea:

```python
return list(map(lambda row: converter(headers, row), rows))
```

La función `map()` aplica la función `converter` a cada fila en la lista `rows`. La función `converter` intenta aplicar los tipos (str, int, float) a cada fila. Pero cuando encuentra una fila con datos faltantes, falla. La función `map()` no tiene una forma incorporada de manejar excepciones. Entonces, cuando se produce una excepción, todo el proceso se bloquea.

En el siguiente paso, modificarás el código para manejar estas excepciones de manera elegante. Esto significa que en lugar de bloquearse, el programa podrá manejar los errores y continuar procesando el resto de los datos.
