# Exportando todo desde el paquete

En Python, la organización de paquetes es crucial para gestionar el código de manera efectiva. Ahora, llevaremos la organización de nuestro paquete un paso más allá. Definiremos qué símbolos deben exportarse a nivel de paquete. Exportar símbolos significa hacer ciertas funciones, clases o variables disponibles para otras partes de tu código o para otros desarrolladores que puedan utilizar tu paquete.

## Agregando `__all__` al paquete

Cuando trabajas con paquetes de Python, es posible que desees controlar qué símbolos son accesibles cuando alguien utiliza la declaración `from structly import *`. Aquí es donde la lista `__all__` resulta útil. Al agregar una lista `__all__` al archivo `__init__.py` del paquete, puedes controlar precisamente qué símbolos están disponibles cuando alguien utiliza la declaración `from structly import *`.

Primero, creemos o actualicemos el archivo `__init__.py`. Usaremos el comando `touch` para crear el archivo si no existe.

```bash
touch ~/project/structly/__init__.py
```

Ahora, abre el archivo `__init__.py` y agrega una lista `__all__`. Esta lista debe incluir todos los símbolos que queremos exportar. Los símbolos se agrupan según de dónde provienen, como los módulos `structure`, `reader` y `tableformat`.

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

Después de agregar el código, guarda el archivo y cierra el editor.

## Entendiendo `import *`

El patrón `from module import *` generalmente no se recomienda en la mayoría del código Python. Hay varias razones para esto:

1. Puede contaminar tu espacio de nombres con símbolos inesperados. Esto significa que podrías terminar con variables o funciones en tu espacio de nombres actual que no esperabas, lo que puede provocar conflictos de nombres.
2. Hace que sea poco claro de dónde provienen ciertos símbolos. Cuando se utiliza `import *`, es difícil saber de qué módulo proviene un símbolo, lo que puede hacer que tu código sea más difícil de entender y mantener.
3. Puede provocar problemas de sombreado (shadowing). El sombreado ocurre cuando una variable o función local tiene el mismo nombre que una variable o función de otro módulo, lo que puede causar un comportamiento inesperado.

Sin embargo, hay casos específicos en los que es adecuado utilizar `import *`:

- Para paquetes diseñados para ser utilizados como un todo cohesivo. Si un paquete está destinado a ser utilizado como una unidad única, entonces utilizar `import *` puede facilitar el acceso a todos los símbolos necesarios.
- Cuando un paquete define una interfaz clara a través de `__all__`. Al utilizar la lista `__all__`, puedes controlar qué símbolos se exportan, lo que hace que sea más seguro utilizar `import *`.
- Para uso interactivo, como en un REPL (Read-Eval-Print Loop) de Python. En un entorno interactivo, puede ser conveniente importar todos los símbolos a la vez.

## Prueba con Import \*

Para verificar que podemos importar todos los símbolos a la vez, creemos otro archivo de prueba. Usaremos el comando `touch` para crear el archivo.

```bash
touch ~/project/test_import_all.py
```

Ahora, abre el archivo `test_import_all.py` y agrega el siguiente contenido. Este código importa todos los símbolos del paquete `structly` y luego prueba si algunos de los símbolos importantes están disponibles.

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

Guarda el archivo y cierra el editor. Ahora, ejecutemos la prueba. Primero, navega al directorio del proyecto utilizando el comando `cd` y luego ejecuta el script de Python.

```bash
cd ~/project
python test_import_all.py
```

Si todo está configurado correctamente, deberías ver una confirmación de que todos los símbolos se importaron correctamente.
