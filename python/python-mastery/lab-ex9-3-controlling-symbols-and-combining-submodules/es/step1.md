# Comprendiendo la complejidad de las importaciones de paquetes

Cuando empieces a trabajar con paquetes de Python, rápidamente te darás cuenta de que importar módulos puede volverse bastante complicado y prolijo. Esta complejidad puede hacer que tu código sea más difícil de leer y escribir. En este laboratorio, analizaremos de cerca este problema y aprenderemos cómo simplificar el proceso de importación.

## Estructura actual de importación

Primero, abramos la terminal. La terminal es una herramienta poderosa que te permite interactuar con el sistema operativo de tu computadora. Una vez abierta la terminal, necesitamos navegar hasta el directorio del proyecto. El directorio del proyecto es donde se almacenan todos los archivos relacionados con nuestro proyecto de Python. Para hacer esto, usaremos el comando `cd`, que significa "cambiar directorio".

```bash
cd ~/project
```

Ahora que estamos en el directorio del proyecto, examinemos la estructura actual del paquete `structly`. Un paquete en Python es una forma de organizar módulos relacionados. Podemos usar el comando `ls -la` para listar todos los archivos y directorios dentro del paquete `structly`, incluyendo los archivos ocultos.

```bash
ls -la structly
```

Notarás que hay varios módulos de Python dentro del paquete `structly`. Estos módulos contienen funciones y clases que podemos usar en nuestro código. Sin embargo, si queremos usar la funcionalidad de estos módulos, actualmente necesitamos usar declaraciones de importación largas. Por ejemplo:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Estas rutas de importación largas pueden ser un problema para escribir, especialmente si necesitas usarlas varias veces en tu código. También hacen que tu código sea menos legible, lo que puede ser un problema cuando estás tratando de entender o depurar tu código. En este laboratorio, aprenderemos cómo organizar el paquete de manera que estas importaciones sean más simples.

Empecemos por echar un vistazo al contenido del archivo `__init__.py` del paquete. El archivo `__init__.py` es un archivo especial en los paquetes de Python. Se ejecuta cuando se importa el paquete y se puede usar para inicializar el paquete y configurar cualquier importación necesaria.

```bash
cat structly/__init__.py
```

Lo más probable es que encuentres que el archivo `__init__.py` está vacío o contiene muy poco código. En los siguientes pasos, modificaremos este archivo para simplificar nuestras declaraciones de importación.

## El objetivo

Al final de este laboratorio, nuestro objetivo es poder usar declaraciones de importación mucho más simples. En lugar de las rutas de importación largas que vimos anteriormente, podremos usar declaraciones como:

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

O incluso:

```python
from structly import *
```

Usar estas declaraciones de importación más simples hará que nuestro código sea más limpio y fácil de manejar. También nos ahorrará tiempo y esfuerzo al escribir y mantener nuestro código.
