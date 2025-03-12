# Aplicaciones prácticas de la gestión de generadores

En este paso, exploraremos cómo aplicar los conceptos que hemos aprendido sobre la gestión de generadores y el manejo de excepciones en generadores a escenarios del mundo real. Comprender estas aplicaciones prácticas te ayudará a escribir código Python más robusto y eficiente.

## Crear un sistema de monitoreo de archivos robusto

Construyamos una versión más confiable de nuestro sistema de monitoreo de archivos. Este sistema será capaz de manejar diferentes situaciones, como tiempos de espera (timeouts) y solicitudes del usuario para detenerlo.

Primero, abre el editor WebIDE y crea un nuevo archivo llamado `robust_follow.py`. Aquí está el código que debes escribir en este archivo:

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

En este código, primero definimos una clase personalizada `TimeoutError`. La función `timeout_handler` se utiliza para lanzar este error cuando se produce un tiempo de espera. La función `follow` es un generador que lee un archivo y produce nuevas líneas. Si se especifica un tiempo de espera, configura una alarma utilizando el módulo `signal`. Si no hay nuevos datos en el archivo, espera un corto tiempo antes de intentarlo de nuevo. El bloque `try - except - finally` se utiliza para manejar diferentes excepciones y garantizar una limpieza adecuada.

Después de escribir el código, guarda el archivo.

## Experimentar con el sistema de monitoreo de archivos robusto

Ahora, probemos nuestro sistema de monitoreo de archivos mejorado. Abre una terminal y ejecuta el intérprete de Python con los siguientes comandos:

```bash
cd ~/project
python3
```

### Experimento 1: Uso básico

En el intérprete de Python, probaremos la funcionalidad básica de nuestro generador `follow`. Aquí está el código a ejecutar:

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Aquí, importamos la función `follow` de nuestro archivo `robust_follow.py`. Luego creamos un objeto generador `f` que sigue el archivo `stocklog.csv`. Usamos un bucle `for` para iterar sobre las líneas producidas por el generador e imprimimos las primeras tres líneas.

### Experimento 2: Uso del tiempo de espera

Veamos cómo funciona la función de tiempo de espera. Ejecuta el siguiente código en el intérprete de Python:

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

En este experimento, creamos un generador con un tiempo de espera de 3 segundos. Procesamos cada línea lentamente, esperando 1 segundo entre cada línea. Después de aproximadamente 3 segundos, el generador lanza una excepción de tiempo de espera y se ejecuta el código de limpieza en el bloque `finally`.

### Experimento 3: Cierre explícito

Probemos cómo el generador maneja un cierre explícito. Ejecuta el siguiente código:

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Aquí, creamos un generador y comenzamos a iterar sobre sus líneas. Después de procesar dos líneas, cerramos explícitamente el generador utilizando el método `close`. El generador luego maneja la excepción `GeneratorExit` y realiza la limpieza necesaria.

## Crear una tubería de procesamiento de datos con manejo de errores

A continuación, crearemos una simple tubería de procesamiento de datos utilizando corutinas. Esta tubería será capaz de manejar errores en diferentes etapas.

Abre el editor WebIDE y crea un nuevo archivo llamado `pipeline.py`. Aquí está el código a escribir en este archivo:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

En este código, el decorador `consumer` se utiliza para inicializar corutinas. La corutina `grep` filtra las líneas que contienen un patrón específico y las envía a otra corutina. La corutina `printer` imprime los elementos recibidos. La función `follow_and_process` lee un archivo, filtra sus líneas utilizando la corutina `grep` e imprime las líneas coincidentes utilizando la corutina `printer`. También maneja la excepción `KeyboardInterrupt` y garantiza una limpieza adecuada.

Después de escribir el código, guarda el archivo.

## Probar la tubería de procesamiento de datos

Probemos nuestra tubería de procesamiento de datos. En una terminal, ejecuta el siguiente comando:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

Deberías ver una salida similar a esta:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Esta salida muestra que la tubería está funcionando correctamente, filtrando e imprimiendo las líneas que contienen el patrón "IBM".

Para detener el proceso, presiona `Ctrl+C`. Deberías ver el siguiente mensaje:

```
Processing stopped by user
```

## Puntos clave

1. El manejo adecuado de excepciones en generadores te permite crear sistemas robustos que pueden manejar errores de manera elegante. Esto significa que tus programas no se bloquearán inesperadamente cuando algo salga mal.
2. Puedes utilizar técnicas como los tiempos de espera para evitar que los generadores se ejecuten indefinidamente. Esto ayuda a administrar los recursos del sistema y garantiza que tu programa no se quede atrapado en un bucle infinito.
3. Los generadores y las corutinas pueden formar poderosas tuberías de procesamiento de datos donde los errores pueden propagarse y manejarse en el nivel adecuado. Esto facilita la construcción de sistemas de procesamiento de datos complejos.
4. El bloque `finally` en los generadores garantiza que se realicen operaciones de limpieza, independientemente de cómo se termine el generador. Esto ayuda a mantener la integridad de tu programa y evita fugas de recursos.
