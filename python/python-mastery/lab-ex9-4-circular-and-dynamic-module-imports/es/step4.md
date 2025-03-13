# Usando importaciones dinámicas

En la programación, las importaciones se utilizan para traer código de otros módulos para que podamos utilizar su funcionalidad. Sin embargo, a veces tener importaciones en medio de un archivo puede hacer que el código sea un poco desordenado y difícil de entender. En esta parte, aprenderemos cómo usar importaciones dinámicas para resolver este problema. Las importaciones dinámicas son una característica poderosa que nos permite cargar módulos en tiempo de ejecución, lo que significa que solo cargamos un módulo cuando realmente lo necesitamos.

Primero, necesitamos eliminar las declaraciones de importación que actualmente se encuentran después de la clase `TableFormatter`. Estas importaciones son importaciones estáticas, que se cargan cuando el programa se inicia. Para hacer esto, abre el archivo `tableformat/formatter.py` en el WebIDE. Una vez que hayas abierto el archivo, encuentra y elimina las siguientes líneas:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Si intentas ejecutar el programa ahora ejecutando el siguiente comando en la terminal:

```bash
python3 stock.py
```

El programa fallará. La razón es que los formateadores no se registrarán en el diccionario `_formats`. Verás un mensaje de error sobre un formato desconocido. Esto se debe a que el programa no puede encontrar las clases de formateadores que necesita para funcionar correctamente.

Para solucionar este problema, modificaremos la función `create_formatter`. El objetivo es importar dinámicamente el módulo necesario cuando sea necesario. Actualiza la función como se muestra a continuación:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

La línea más importante en esta función es:

```python
__import__(f'{__package__}.formats.{name}')
```

Esta línea importa dinámicamente el módulo basado en el nombre del formato. Cuando se importa el módulo, su subclase de `TableFormatter` se registra automáticamente. Esto se debe al método `__init_subclass__` que agregamos anteriormente. Este método es un método especial de Python que se llama cuando se crea una subclase, y en nuestro caso, se utiliza para registrar la clase de formateador.

Después de hacer estos cambios, guarda el archivo. Luego, ejecuta el programa nuevamente utilizando el siguiente comando:

```bash
python3 stock.py
```

El programa ahora debería funcionar correctamente, incluso aunque hayamos eliminado las importaciones estáticas. Para verificar que la importación dinámica está funcionando como se espera, limpiaremos el diccionario `_formats` y luego llamaremos a la función `create_formatter`. Ejecuta el siguiente comando en la terminal:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

Deberías ver una salida similar a esta:

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

Esta salida confirma que la importación dinámica está cargando el módulo y registrando la clase de formateador cuando es necesario.

Al usar importaciones dinámicas y registro de clases, hemos creado una estructura de código más limpia y fácil de mantener. Estos son los beneficios:

1. Todas las importaciones ahora están en la parte superior del archivo, lo que sigue las convenciones de Python. Esto hace que el código sea más fácil de leer y entender.
2. Hemos eliminado las importaciones circulares. Las importaciones circulares pueden causar problemas en un programa, como bucles infinitos o errores difíciles de depurar.
3. El código es más flexible. Ahora, podemos agregar nuevos formateadores sin modificar la función `create_formatter`. Esto es muy útil en un escenario del mundo real donde se pueden agregar nuevas características con el tiempo.

Este patrón de uso de importaciones dinámicas y registro de clases se utiliza comúnmente en sistemas de complementos (plugins) y marcos de trabajo (frameworks). En estos sistemas, los componentes deben cargarse dinámicamente según las necesidades del usuario o los requisitos del programa.
