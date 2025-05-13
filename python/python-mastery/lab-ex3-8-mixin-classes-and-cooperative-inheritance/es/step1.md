# Entendiendo el Problema con el Formato de Columnas

En este paso, vamos a analizar una limitación en nuestra implementación actual del formato de tablas. También examinaremos algunas posibles soluciones a este problema.

Primero, entendamos lo que vamos a hacer. Abriremos el editor VSCode y examinaremos el archivo `tableformat.py` en el directorio del proyecto. Este archivo es importante porque contiene el código que nos permite formatear datos tabulares de diferentes maneras, como en formatos de texto, CSV o HTML.

Para abrir el archivo, usaremos los siguientes comandos en la terminal. El comando `cd` cambia el directorio al directorio del proyecto, y el comando `code` abre el archivo `tableformat.py` en VSCode.

```bash
cd ~/project
touch tableformat.py
```

Cuando abras el archivo, notarás que hay varias clases definidas. Estas clases juegan diferentes roles en el formateo de los datos de la tabla.

- `TableFormatter`: Esta es una clase base abstracta. Tiene métodos que se utilizan para formatear los encabezados y las filas de la tabla. Piénsalo como un plano para otras clases de formateadores (formatter classes).
- `TextTableFormatter`: Esta clase se utiliza para mostrar la tabla en formato de texto plano.
- `CSVTableFormatter`: Es responsable de formatear los datos de la tabla en formato CSV (Comma-Separated Values - Valores Separados por Comas).
- `HTMLTableFormatter`: Esta clase formatea los datos de la tabla en formato HTML.

También hay una función `print_table()` en el archivo. Esta función utiliza las clases de formateadores que acabamos de mencionar para mostrar los datos tabulares.

Ahora, veamos cómo funcionan estas clases. En tu directorio `/home/labex/project`, crea un nuevo archivo llamado `step1_test1.py` usando tu editor o el comando `touch`. Agrega el siguiente código Python:

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Guarda el archivo y ejecútalo desde tu terminal:

```bash
python3 step1_test1.py
```

Después de ejecutar el script, deberías ver una salida similar a esta:

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Ahora, encontremos el problema. Observa que los valores en la columna `price` no están formateados de manera consistente. Algunos valores tienen un decimal, como 32.2, mientras que otros tienen dos decimales, como 51.23. En los datos financieros, generalmente queremos que el formato sea consistente.

Esto es lo que queremos que se vea la salida:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Una forma de solucionar esto es modificar la función `print_table()` para que acepte especificaciones de formato. Veamos cómo funciona esto _sin_ modificar realmente `tableformat.py`. Crea un nuevo archivo llamado `step1_test2.py` con el siguiente contenido. Este script redefine la función `print_table` localmente con fines de demostración.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Ejecuta este script:

```bash
python3 step1_test2.py
```

Este enfoque demuestra el paso de formatos, pero modificar `print_table` tiene un inconveniente: cambiar la interfaz de la función podría romper el código existente que utiliza la versión original.

Otro enfoque es crear un formateador personalizado (custom formatter) mediante la creación de subclases (subclassing). Podemos crear una nueva clase que herede de `TextTableFormatter` y anule (override) el método `row()`. Crea un archivo `step1_test3.py`:

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Ejecuta el script:

```bash
python3 step1_test3.py
```

Esta solución funciona para demostrar la creación de subclases, pero crear una nueva clase para cada variación de formato no es conveniente. Además, estás atado a la clase base de la que heredas (aquí, `TextTableFormatter`).

En el siguiente paso, exploraremos una solución más elegante utilizando clases mixin.
