# Creación de una API Fácil de Usar para Mixins

Los mixins son poderosos, pero usar la herencia múltiple directamente puede sentirse complejo. En este paso, mejoraremos la función `create_formatter()` para ocultar esta complejidad, proporcionando una API más fácil para los usuarios.

Primero, asegúrate de que `tableformat.py` esté abierto en tu editor:

```bash
cd ~/project
touch tableformat.py
```

Encuentra la función `create_formatter()` existente:

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Reemplaza _toda la definición existente_ de la función `create_formatter()` con la versión mejorada a continuación. Esta nueva versión acepta argumentos opcionales para formatos de columna y encabezados en mayúsculas.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_Autocorrección: Crea dinámicamente la tupla de clase para la herencia en lugar de múltiples ramas if/elif._

Esta función mejorada primero determina la clase formateadora base (`TextTableFormatter`, `CSVTableFormatter`, etc.). Luego, basándose en los argumentos opcionales `column_formats` y `upper_headers`, construye dinámicamente una nueva clase (`CustomFormatter`) que hereda de los mixins necesarios y la clase formateadora base. Finalmente, devuelve una instancia de este formateador personalizado.

**Recuerda guardar los cambios en `tableformat.py`.**

Ahora, probemos nuestra función mejorada. **Asegúrate de haber guardado la función `create_formatter` actualizada en `tableformat.py`.**

Primero, prueba el formato de columna. Crea `step3_test1.py`:

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Ejecuta el script:

```bash
python3 step3_test1.py
```

Deberías ver la tabla con las columnas formateadas (nuevamente, sujeto al manejo de tipos del formato de precio):

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

A continuación, prueba los encabezados en mayúsculas. Crea `step3_test2.py`:

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Ejecuta el script:

```bash
python3 step3_test2.py
```

Deberías ver la tabla con los encabezados en mayúsculas:

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Finalmente, combina ambas opciones. Crea `step3_test3.py`:

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Ejecuta el script:

```bash
python3 step3_test3.py
```

Esto debería mostrar una tabla con columnas formateadas y encabezados en mayúsculas:

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
------------------------------------------------------------------
```

La función mejorada también funciona con otros tipos de formateadores. Por ejemplo, pruébalo con el formateador CSV. Crea `step3_test4.py`:

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Ejecuta el script:

```bash
python3 step3_test4.py
```

Esto debería producir encabezados en mayúsculas y columnas formateadas en formato CSV (nuevamente, posible problema de tipo para el formato `%d`/`%.2f` en cadenas pasadas desde `print_table`):

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

Al mejorar la función `create_formatter()`, hemos creado una API fácil de usar. Los usuarios ahora pueden aplicar fácilmente las funcionalidades de mixin sin necesidad de administrar la estructura de herencia múltiple ellos mismos.
