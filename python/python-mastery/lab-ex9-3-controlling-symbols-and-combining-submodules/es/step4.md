# División de módulos para una mejor organización del código

A medida que crecen tus proyectos de Python, es posible que descubras que un solo archivo de módulo se vuelve bastante grande y contiene múltiples componentes relacionados pero distintos. Cuando esto sucede, es una buena práctica dividir el módulo en un paquete con submódulos. Este enfoque hace que tu código esté más organizado, sea más fácil de mantener y sea más escalable.

## Comprendiendo la estructura actual

El módulo `tableformat.py` es un buen ejemplo de un módulo grande. Contiene varias clases de formateadores, cada una responsable de formatear datos de una manera diferente:

- `TableFormatter` (clase base): Esta es la clase base para todas las demás clases de formateadores. Define la estructura básica y los métodos que las otras clases heredarán e implementarán.
- `TextTableFormatter`: Esta clase formatea los datos en texto plano.
- `CSVTableFormatter`: Esta clase formatea los datos en formato CSV (Comma-Separated Values, valores separados por comas).
- `HTMLTableFormatter`: Esta clase formatea los datos en formato HTML (Hypertext Markup Language, lenguaje de marcado de hipertexto).

Reorganizaremos este módulo en una estructura de paquete con archivos separados para cada tipo de formateador. Esto hará que el código sea más modular y más fácil de gestionar.

## Paso 1: Limpiar archivos de caché

Antes de comenzar a reorganizar el código, es una buena idea limpiar cualquier archivo de caché de Python. Estos archivos son creados por Python para acelerar la ejecución de tu código, pero a veces pueden causar problemas cuando estás realizando cambios en tu código.

```bash
cd ~/project/structly
rm -rf __pycache__
```

En los comandos anteriores, `cd ~/project/structly` cambia el directorio actual al directorio `structly` de tu proyecto. `rm -rf __pycache__` elimina el directorio `__pycache__` y todo su contenido. La opción `-r` significa recursivo, lo que significa que eliminará todos los archivos y subdirectorios dentro del directorio `__pycache__`. La opción `-f` significa forzar, lo que significa que eliminará los archivos sin pedir confirmación.

## Paso 2: Crear la nueva estructura de paquete

Ahora, creemos una nueva estructura de directorios para nuestro paquete. Crearemos un directorio llamado `tableformat` y un subdirectorio llamado `formats` dentro de él.

```bash
mkdir -p tableformat/formats
```

El comando `mkdir` se utiliza para crear directorios. La opción `-p` significa padres, lo que significa que creará todos los directorios padres necesarios si no existen. Entonces, si el directorio `tableformat` no existe, se creará primero, y luego se creará el directorio `formats` dentro de él.

## Paso 3: Mover y renombrar el archivo original

A continuación, moveremos el archivo original `tableformat.py` a la nueva estructura y lo renombraremos a `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

El comando `mv` se utiliza para mover o renombrar archivos. En este caso, estamos moviendo el archivo `tableformat.py` al directorio `tableformat` y renombrándolo a `formatter.py`.

## Paso 4: Dividir el código en archivos separados

Ahora necesitamos crear archivos para cada formateador y mover el código relevante a ellos.

### 1. Crear el archivo del formateador base

```bash
touch tableformat/formatter.py
```

El comando `touch` se utiliza para crear un archivo vacío. En este caso, estamos creando un archivo llamado `formatter.py` en el directorio `tableformat`.

Mantendremos la clase base `TableFormatter` y cualquier función de utilidad general como `print_table` y `create_formatter` en este archivo. El archivo debería verse algo así:

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

La variable `__all__` se utiliza para especificar qué símbolos deben importarse cuando se utiliza `from module import *`. En este caso, estamos especificando que solo se deben importar los símbolos `TableFormatter`, `print_table` y `create_formatter`.

La clase `TableFormatter` es la clase base para todas las demás clases de formateadores. Define dos métodos, `headings` y `row`, que están destinados a ser implementados por las subclases.

La función `print_table` es una función de utilidad que toma una lista de objetos, una lista de nombres de columnas y un objeto formateador, y muestra los datos en una tabla formateada.

La función `create_formatter` es una función fábrica que toma un nombre de formato como argumento y devuelve un objeto formateador adecuado.

Guarda y cierra el archivo después de realizar estos cambios.

### 2. Crear el formateador de texto

```bash
touch tableformat/formats/text.py
```

Agregaremos solo la clase `TextTableFormatter` a este archivo.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

La variable `__all__` especifica que solo se debe importar el símbolo `TextTableFormatter` cuando se utiliza `from module import *`.

La declaración `from ..formatter import TableFormatter` importa la clase `TableFormatter` del archivo `formatter.py` en el directorio padre.

La clase `TextTableFormatter` hereda de la clase `TableFormatter` e implementa los métodos `headings` y `row` para formatear los datos en texto plano.

Guarda y cierra el archivo después de realizar estos cambios.

### 3. Crear el formateador de CSV

```bash
touch tableformat/formats/csv.py
```

Agregaremos solo la clase `CSVTableFormatter` a este archivo.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

Similar a los pasos anteriores, estamos especificando la variable `__all__`, importando la clase `TableFormatter` e implementando los métodos `headings` y `row` para formatear los datos en formato CSV.

Guarda y cierra el archivo después de realizar estos cambios.

### 4. Crear el formateador de HTML

```bash
touch tableformat/formats/html.py
```

Agregaremos solo la clase `HTMLTableFormatter` a este archivo.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Nuevamente, estamos especificando la variable `__all__`, importando la clase `TableFormatter` e implementando los métodos `headings` y `row` para formatear los datos en formato HTML.

Guarda y cierra el archivo después de realizar estos cambios.

## Paso 5: Crear archivos de inicialización de paquete

En Python, los archivos `__init__.py` se utilizan para marcar directorios como paquetes de Python. Necesitamos crear archivos `__init__.py` tanto en el directorio `tableformat` como en el directorio `formats`.

### 1. Crear uno para el paquete `tableformat`

```bash
touch tableformat/__init__.py
```

Agrega este contenido al archivo:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Esta declaración importa todos los símbolos del archivo `formatter.py` y los hace disponibles cuando se importa el paquete `tableformat`.

Guarda y cierra el archivo después de realizar estos cambios.

### 2. Crear uno para el paquete `formats`

```bash
touch tableformat/formats/__init__.py
```

Puedes dejar este archivo vacío o agregar una simple cadena de documentación (docstring):

```python
'''
Format implementations for different output formats.
'''
```

La cadena de documentación proporciona una breve descripción de lo que hace el paquete `formats`.

Guarda y cierra el archivo después de realizar estos cambios.

## Paso 6: Probar la nueva estructura

Creemos una prueba sencilla para verificar que nuestros cambios funcionen correctamente.

```bash
cd ~/project
touch test_tableformat.py
```

Agrega este contenido al archivo `test_tableformat.py`:

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

Este código de prueba importa las funciones y clases necesarias del paquete `structly`, crea formateadores de cada tipo, define algunos datos de prueba y luego prueba cada formateador mostrando los datos en el formato correspondiente.

Guarda y cierra el archivo después de realizar estos cambios. Ahora ejecuta la prueba:

```bash
python test_tableformat.py
```

Deberías ver los mismos datos formateados de tres maneras diferentes (texto, CSV y HTML). Si ves la salida esperada, significa que la reorganización de tu código fue exitosa.
