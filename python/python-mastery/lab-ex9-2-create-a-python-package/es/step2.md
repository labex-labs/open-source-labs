# Creación de la estructura del paquete

Ahora, vamos a crear nuestro paquete de Python. Pero primero, entendamos qué es un paquete de Python. Un paquete de Python es una forma de organizar módulos de Python relacionados en una única jerarquía de directorios. Ayuda a gestionar y reutilizar el código de manera más efectiva. Para crear un paquete de Python, necesitamos seguir estos pasos:

1. Crear un directorio con el nombre del paquete. Este directorio servirá como contenedor para todos los módulos que pertenecen al paquete.
2. Crear un archivo `__init__.py` dentro de este directorio. Este archivo es crucial porque hace que Python reconozca el directorio como un paquete. Cuando se importa el paquete, se ejecuta el código en `__init__.py`, que se puede utilizar para inicializar el paquete.
3. Mover nuestros archivos de módulos de Python a este directorio. Este paso asegura que todo el código relacionado se agrupe dentro del paquete.

Vamos a crear la estructura del paquete paso a paso:

1. Primero, crea un directorio llamado `structly`. Este será el directorio raíz de nuestro paquete.

```bash
mkdir structly
```

2. A continuación, crea un archivo `__init__.py` vacío dentro del directorio `structly`.

```bash
touch structly/__init__.py
```

El archivo `__init__.py` puede estar vacío, pero es necesario para que Python trate el directorio como un paquete. Cuando se importa el paquete, se ejecuta el código en `__init__.py`, que se puede utilizar para inicializar el paquete.

3. Ahora, vamos a mover nuestros archivos de módulos de Python al directorio `structly`. Estos archivos de módulos contienen las funciones y clases que queremos incluir en nuestro paquete.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Verifica que todos los archivos se hayan movido correctamente. Podemos usar el comando `ls -l` para listar el contenido del directorio `structly`.

```bash
ls -l structly/
```

Deberías ver los siguientes archivos listados:

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

Ahora hemos creado una estructura básica de paquete. La jerarquía de directorios debería verse así:

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

En el siguiente paso, corregiremos las declaraciones de importación para que el paquete funcione correctamente.
