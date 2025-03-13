# Control de símbolos exportados con `__all__`

En Python, cuando se utiliza la declaración `from module import *`, es posible que desees controlar qué símbolos (funciones, clases, variables) se importan de un módulo. Aquí es donde la variable `__all__` resulta útil. La declaración `from module import *` es una forma de importar todos los símbolos de un módulo al espacio de nombres actual. Sin embargo, a veces no se desea importar cada símbolo, especialmente si hay muchos o si algunos están destinados a ser internos del módulo. La variable `__all__` te permite especificar exactamente qué símbolos deben importarse cuando se utiliza esta declaración.

## ¿Qué es `__all__`?

La variable `__all__` es una lista de cadenas. Cada cadena en esta lista representa un símbolo (función, clase o variable) que un módulo exporta cuando alguien utiliza la declaración `from module import *`. Si la variable `__all__` no está definida en un módulo, la declaración `import *` importará todos los símbolos que no comiencen con un guión bajo. Los símbolos que comienzan con un guión bajo generalmente se consideran privados o internos del módulo y no están destinados a ser importados directamente.

## Modificación de cada submódulo

Ahora, agreguemos la variable `__all__` a cada submódulo en el paquete `structly`. Esto nos ayudará a controlar qué símbolos se exportan de cada submódulo cuando alguien utiliza la declaración `from module import *`.

1. Primero, modifiquemos `structure.py`:

```bash
touch ~/project/structly/structure.py
```

Este comando crea un nuevo archivo llamado `structure.py` en el directorio `structly` de tu proyecto. Después de crear el archivo, necesitamos agregar la variable `__all__`. Agrega esta línea cerca de la parte superior del archivo, justo después de las declaraciones de importación:

```python
__all__ = ['Structure']
```

Esta línea le dice a Python que cuando alguien utilice `from structure import *`, solo se importará el símbolo `Structure`. Guarda el archivo y cierra el editor.

2. A continuación, modifiquemos `reader.py`:

```bash
touch ~/project/structly/reader.py
```

Este comando crea un nuevo archivo llamado `reader.py` en el directorio `structly`. Ahora, revisa el archivo para encontrar todas las funciones que comiencen con `read_csv_as_`. Estas son las funciones que queremos exportar. Luego, agrega una lista `__all__` con todos los nombres de estas funciones. Debería verse algo así:

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

Ten en cuenta que los nombres reales de las funciones pueden variar dependiendo de lo que encuentres en el archivo. Asegúrate de incluir todas las funciones `read_csv_as_*` que encuentres. Guarda el archivo y cierra el editor.

3. Ahora, modifiquemos `tableformat.py`:

```bash
touch ~/project/structly/tableformat.py
```

Este comando crea un nuevo archivo llamado `tableformat.py` en el directorio `structly`. Agrega esta línea cerca de la parte superior del archivo:

```python
__all__ = ['create_formatter', 'print_table']
```

Esta línea especifica que cuando alguien utilice `from tableformat import *`, solo se importarán los símbolos `create_formatter` y `print_table`. Guarda el archivo y cierra el editor.

## Importaciones unificadas en `__init__.py`

Ahora que cada módulo define lo que exporta, podemos actualizar el archivo `__init__.py` para importar todos estos símbolos. El archivo `__init__.py` es un archivo especial en los paquetes de Python. Se ejecuta cuando se importa el paquete y se puede utilizar para inicializar el paquete e importar símbolos de los submódulos.

```bash
touch ~/project/structly/__init__.py
```

Este comando crea un nuevo archivo `__init__.py` en el directorio `structly`. Cambia el contenido del archivo a:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Estas líneas importan todos los símbolos exportados de los submódulos `structure`, `reader` y `tableformat`. El punto (`.`) antes de los nombres de los módulos indica que son importaciones relativas, lo que significa que son importaciones desde dentro del mismo paquete. Guarda el archivo y cierra el editor.

## Prueba de nuestros cambios

Creemos un archivo de prueba sencillo para verificar que nuestros cambios funcionen. Este archivo de prueba intentará importar los símbolos que especificamos en las variables `__all__` e imprimirá un mensaje de éxito si las importaciones son exitosas.

```bash
touch ~/project/test_structly.py
```

Este comando crea un nuevo archivo llamado `test_structly.py` en el directorio del proyecto. Agrega este contenido al archivo:

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

Estas líneas intentan importar la clase `Structure`, la función `read_csv_as_instances` y las funciones `create_formatter` y `print_table` del paquete `structly`. Si las importaciones son exitosas, el programa imprimirá el mensaje "Successfully imported all required symbols!". Guarda el archivo y cierra el editor. Ahora ejecutemos esta prueba:

```bash
cd ~/project
python test_structly.py
```

El comando `cd ~/project` cambia el directorio de trabajo actual al directorio del proyecto. El comando `python test_structly.py` ejecuta el script `test_structly.py`. Si todo está funcionando correctamente, deberías ver el mensaje "Successfully imported all required symbols!" impreso en la pantalla.
