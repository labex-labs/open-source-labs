# Comprendiendo el problema de importación

Comencemos por entender qué son las importaciones de módulos. En Python, cuando quieres utilizar funciones, clases o variables de otro archivo (módulo), se utiliza la declaración `import`. Sin embargo, la forma en que estructuras tus importaciones puede generar diversos problemas.

Ahora, vamos a examinar un ejemplo de una estructura de módulo problemática. El código en `tableformat/formatter.py` tiene importaciones dispersas a lo largo del archivo. Esto puede no parecer un gran problema al principio, pero crea problemas de mantenimiento y dependencias.

Primero, abre el explorador de archivos del WebIDE y navega hasta el directorio `structly`. Ejecutaremos un par de comandos para entender la estructura actual del proyecto. El comando `cd` se utiliza para cambiar el directorio de trabajo actual, y el comando `ls -la` lista todos los archivos y directorios en el directorio actual, incluyendo los ocultos.

```bash
cd ~/project/structly
ls -la
```

Esto mostrará los archivos en el directorio del proyecto. Ahora, vamos a ver uno de los archivos problemáticos utilizando el comando `cat`, que muestra el contenido de un archivo.

```bash
cat tableformat/formatter.py
```

Deberías ver un código similar al siguiente:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Observa la ubicación de las declaraciones de importación en medio del archivo. Esto es problemático por varios motivos:

1. Hace que el código sea más difícil de leer y mantener. Cuando se mira un archivo, se espera ver todas las importaciones al principio para poder entender rápidamente de qué módulos externos depende el archivo.
2. Puede generar problemas de importación circular. Las importaciones circulares ocurren cuando dos o más módulos dependen entre sí, lo que puede causar errores y hacer que tu código se comporte de manera inesperada.
3. Rompe la convención de Python de colocar todas las importaciones en la parte superior de un archivo. Seguir las convenciones hace que tu código sea más legible y más fácil de entender para otros desarrolladores.

En los siguientes pasos, exploraremos estos problemas en más detalle y aprenderemos cómo resolverlos.
