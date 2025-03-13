# Implementando el registro de subclases

En la programación, las importaciones circulares pueden ser un problema complicado. En lugar de importar directamente las clases de formateadores, podemos utilizar un patrón de registro. En este patrón, las subclases se registran a sí mismas con su clase padre. Esta es una forma común y efectiva de evitar las importaciones circulares.

Primero, entendamos cómo podemos averiguar el nombre del módulo de una clase. El nombre del módulo es importante porque lo usaremos en nuestro patrón de registro. Para hacer esto, ejecutaremos un comando de Python en la terminal.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

Cuando ejecutes este comando, verás una salida como esta:

```
structly.tableformat.formats.text
text
```

Esta salida muestra que podemos extraer el nombre del módulo de la propia clase. Usaremos este nombre de módulo más adelante para registrar las subclases.

Ahora, modifiquemos la clase `TableFormatter` en el archivo `tableformat/formatter.py` para agregar un mecanismo de registro. Abre este archivo en el WebIDE. Agregaremos algún código a la clase `TableFormatter`. Este código nos ayudará a registrar las subclases automáticamente.

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

El método `__init_subclass__` es un método especial en Python. Se llama siempre que se crea una subclase de `TableFormatter`. En este método, extraemos el nombre del módulo de la subclase y lo usamos como clave para registrar la subclase en el diccionario `_formats`.

A continuación, necesitamos modificar la función `create_formatter` para usar el diccionario de registro. Esta función es responsable de crear el formateador adecuado basado en el nombre dado.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
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

Después de hacer estos cambios, guarda el archivo. Luego, probemos si el programa sigue funcionando. Ejecutaremos el script `stock.py`.

```bash
python3 stock.py
```

Si el programa se ejecuta correctamente, significa que nuestros cambios no han roto nada. Ahora, echemos un vistazo al contenido del diccionario `_formats` para ver cómo funciona el registro.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

Deberías ver una salida como esta:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

Esta salida confirma que nuestras subclases se están registrando correctamente en el diccionario `_formats`. Sin embargo, todavía tenemos algunas importaciones en medio del archivo. En el siguiente paso, solucionaremos este problema utilizando importaciones dinámicas.
