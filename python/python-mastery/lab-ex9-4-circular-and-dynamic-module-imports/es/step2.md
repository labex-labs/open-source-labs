# Explorando las importaciones circulares

Una importación circular es una situación en la que dos o más módulos dependen entre sí. Específicamente, cuando el módulo A importa el módulo B, y el módulo B también importa el módulo A, ya sea directamente o indirectamente. Esto crea un bucle de dependencia que el sistema de importación de Python no puede resolver adecuadamente. En términos más simples, Python se queda atrapado en un bucle tratando de averiguar qué módulo importar primero, y esto puede causar errores en tu programa.

Vamos a experimentar con nuestro código para ver cómo las importaciones circulares pueden causar problemas.

Primero, ejecutaremos el programa de stocks (acciones) para comprobar si funciona con la estructura actual. Este paso nos ayuda a establecer una base y ver el programa funcionando como se espera antes de realizar cualquier cambio.

```bash
cd ~/project/structly
python3 stock.py
```

El programa debería ejecutarse correctamente y mostrar los datos de las acciones en una tabla formateada. Si lo hace, eso significa que la estructura actual del código funciona bien sin ningún problema de importación circular.

Ahora, vamos a modificar el archivo `formatter.py`. Por lo general, es una buena práctica mover las importaciones a la parte superior de un archivo. Esto hace que el código esté más organizado y sea más fácil de entender a simple vista.

```bash
cd ~/project/structly
```

Abre `tableformat/formatter.py` en el WebIDE. Vamos a mover las siguientes importaciones a la parte superior del archivo, justo después de las importaciones existentes. Estas importaciones son para diferentes formateadores de tablas, como texto, CSV y HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Así que el comienzo del archivo ahora debería verse así:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Guarda el archivo y vuelve a intentar ejecutar el programa de stocks.

```bash
python3 stock.py
```

Deberías ver un mensaje de error sobre `TableFormatter` no definido. Esto es una señal clara de un problema de importación circular.

El problema se produce debido a la siguiente cadena de eventos:

1. `formatter.py` intenta importar `TextTableFormatter` de `formats/text.py`.
2. `formats/text.py` importa `TableFormatter` de `formatter.py`.
3. Cuando Python intenta resolver estas importaciones, se queda atrapado en un bucle porque no puede decidir qué módulo importar por completo primero.

Vamos a revertir nuestros cambios para que el programa funcione de nuevo. Edita `tableformat/formatter.py` y mueve las importaciones de vuelta a donde estaban originalmente (después de la definición de la clase `TableFormatter`).

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
```

Ejecuta el programa de nuevo para confirmar que está funcionando.

```bash
python3 stock.py
```

Esto demuestra que aunque tener importaciones en medio del archivo no es la mejor práctica en términos de organización del código, se hizo para evitar un problema de importación circular. En los siguientes pasos, exploraremos mejores soluciones.
