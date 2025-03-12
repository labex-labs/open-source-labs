# Comprender la vida útil y el cierre de los generadores

En este paso, vamos a explorar la vida útil de los generadores de Python y aprender cómo cerrarlos adecuadamente. Los generadores en Python son un tipo especial de iterador que te permite generar una secuencia de valores sobre la marcha, en lugar de calcularlos todos de una vez y almacenarlos en memoria. Esto puede ser muy útil cuando se trabaja con conjuntos de datos grandes o secuencias infinitas.

## ¿Qué es el generador `follow()`?

Comencemos por echar un vistazo al archivo `follow.py` en el directorio del proyecto. Este archivo contiene una función generadora llamada `follow()`. Una función generadora se define como una función normal, pero en lugar de usar la palabra clave `return`, utiliza `yield`. Cuando se llama a una función generadora, devuelve un objeto generador, sobre el cual se puede iterar para obtener los valores que produce.

La función generadora `follow()` lee continuamente líneas de un archivo y produce cada línea a medida que se lee. Esto es similar al comando Unix `tail -f`, que monitorea continuamente un archivo en busca de nuevas líneas.

Abre el archivo `follow.py` en el editor WebIDE:

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

En este código, la declaración `with open(filename, 'r') as f` abre el archivo en modo lectura y asegura que se cierre adecuadamente cuando se sale del bloque. La línea `f.seek(0, os.SEEK_END)` mueve el puntero del archivo al final del archivo, de modo que el generador comience a leer desde el final. El bucle `while True` lee continuamente líneas del archivo. Si la línea está vacía, significa que aún no hay nuevas líneas, por lo que el programa se detiene durante 0.1 segundos para evitar un ciclo activo y luego continúa con la siguiente iteración. Si la línea no está vacía, se produce.

Este generador se ejecuta en un bucle infinito, lo que plantea una pregunta importante: ¿qué sucede cuando dejamos de usar el generador o queremos terminarlo antes?

## Modificar el generador para manejar el cierre

Necesitamos modificar la función `follow()` en `follow.py` para manejar el caso en el que el generador se cierre adecuadamente. Para hacer esto, agregaremos un bloque `try-except` que capture la excepción `GeneratorExit`. La excepción `GeneratorExit` se levanta cuando un generador se cierra, ya sea por recolección de basura o al llamar al método `close()`.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

En este código modificado, el bloque `try` contiene la lógica principal del generador. Si se levanta una excepción `GeneratorExit`, el bloque `except` la captura y muestra el mensaje 'Following Done'. Esta es una forma sencilla de realizar acciones de limpieza cuando se cierra el generador.

Guarda el archivo después de realizar estos cambios.

## Experimentar con el cierre de generadores

Ahora, realicemos algunos experimentos para ver cómo se comportan los generadores cuando son recolectados por el recolector de basura o se cierran explícitamente.

Abre una terminal y ejecuta el intérprete de Python:

```bash
cd ~/project
python3
```

### Experimento 1: Recolección de basura de un generador en ejecución

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

En este experimento, primero importamos la función `follow` del archivo `follow.py`. Luego creamos un objeto generador `f` llamando a `follow('stocklog.csv')`. Usamos la función `next()` para obtener la siguiente línea del generador. Finalmente, eliminamos el objeto generador usando la declaración `del`. Cuando se elimina el objeto generador, se cierra automáticamente, lo que activa nuestro manejador de excepción `GeneratorExit`, y se muestra el mensaje 'Following Done'.

### Experimento 2: Cerrar explícitamente un generador

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

En este experimento, creamos un nuevo objeto generador `f` e iteramos sobre él usando un bucle `for`. Dentro del bucle, imprimimos cada línea y verificamos si la línea contiene la cadena 'IBM'. Si es así, llamamos al método `close()` en el generador para cerrarlo explícitamente. Cuando se cierra el generador, se levanta la excepción `GeneratorExit`, y nuestro manejador de excepciones muestra el mensaje 'Following Done'. Después de que se cierra el generador, si intentamos iterar sobre él nuevamente, no habrá salida porque el generador ya no está activo.

### Experimento 3: Salir y reanudar un generador

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

En este experimento, creamos un objeto generador `f` e iteramos sobre él usando un bucle `for`. Dentro del bucle, imprimimos cada línea y verificamos si la línea contiene la cadena 'IBM'. Si es así, usamos la declaración `break` para salir del bucle. Salir del bucle no cierra el generador, por lo que el generador sigue activo. Luego podemos reanudar la iteración iniciando un nuevo bucle `for` sobre el mismo objeto generador. Finalmente, eliminamos el objeto generador para realizar la limpieza, lo que activa el manejador de excepción `GeneratorExit`.

## Puntos clave

1. Cuando se cierra un generador (ya sea a través de la recolección de basura o llamando a `close()`), se levanta una excepción `GeneratorExit` dentro del generador.
2. Puedes capturar esta excepción para realizar acciones de limpieza cuando se cierra el generador.
3. Salir de la iteración de un generador (con `break`) no cierra el generador, lo que permite reanudarlo más tarde.

Sal del intérprete de Python escribiendo `exit()` o presionando `Ctrl+D`.
