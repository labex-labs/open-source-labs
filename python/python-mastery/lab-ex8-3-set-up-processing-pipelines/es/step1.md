# Comprender las corrutinas con un seguidor de archivos

Comencemos por entender qué son las corrutinas y cómo funcionan en Python. Una corrutina es una versión especializada de una función generadora. En Python, las funciones generalmente comienzan desde el principio cada vez que se llaman. Pero las corrutinas son diferentes. Pueden consumir y producir datos, y tienen la capacidad de suspender y reanudar su ejecución. Esto significa que una corrutina puede pausar su operación en un cierto punto y luego retomar justo donde lo dejó más tarde.

## Crear un seguidor de archivos de corrutina básico

En este paso, crearemos un seguidor de archivos que utiliza corrutinas para monitorear un archivo en busca de nuevo contenido y procesarlo. Esto es similar al comando Unix `tail -f`, que muestra continuamente el final de un archivo y se actualiza a medida que se agregan nuevas líneas.

1. Abre el editor de código y crea un nuevo archivo llamado `cofollow.py` en el directorio `/home/labex/project`. Aquí es donde escribiremos nuestro código Python para implementar el seguidor de archivos utilizando corrutinas.

2. Copia el siguiente código en el archivo:

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. Comprendamos los componentes clave de este código:
   - `follow(filename, target)`: Esta función es responsable de abrir un archivo. Primero mueve el puntero del archivo al final del archivo utilizando `f.seek(0, os.SEEK_END)`. Luego, entra en un bucle infinito donde intenta leer continuamente nuevas líneas del archivo. Si se encuentra una nueva línea, la envía a la corrutina objetivo utilizando el método `send`. Si no hay nuevo contenido, se pausa durante un corto tiempo (0,1 segundos) utilizando `time.sleep(0.1)` antes de volver a comprobar.
   - Decorador `@consumer`: En Python, las corrutinas deben ser "inicializadas" antes de que puedan comenzar a recibir datos. Este decorador se encarga de eso. Envía automáticamente un valor inicial `None` a la corrutina, que es un paso necesario para preparar la corrutina para recibir datos reales.
   - Corrutina `printer()`: Esta es una corrutina simple. Tiene un bucle infinito donde utiliza la palabra clave `yield` para recibir un elemento enviado a ella. Una vez que recibe un elemento, simplemente lo imprime.

4. Guarda el archivo y ejecútalo desde la terminal:

```bash
cd /home/labex/project
python3 cofollow.py
```

5. Deberías ver que el script imprime el contenido del archivo de registro de acciones, y continuará imprimiendo nuevas líneas a medida que se agreguen al archivo. Presiona `Ctrl+C` para detener el programa.

El concepto clave aquí es que los datos fluyen desde la función `follow` hacia la corrutina `printer` a través del método `send`. Este "empuje" de datos es lo contrario de los generadores, que "tiran" datos a través de la iteración. En un generador, normalmente se utiliza un bucle `for` para iterar sobre los valores que produce. Pero en este ejemplo de corrutina, los datos se envían activamente de una parte del código a otra.
