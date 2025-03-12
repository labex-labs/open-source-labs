# Creando una API amigable para los usuarios con mixins

Los mixins son una característica poderosa en Python, pero pueden ser un poco complicados para los principiantes porque involucran herencia múltiple, lo cual puede volverse bastante complejo. En este paso, vamos a facilitar las cosas para los usuarios mejorando la función `create_formatter()`. De esta manera, los usuarios no tendrán que preocuparse demasiado por los detalles de la herencia múltiple.

Primero, necesitas abrir el archivo `tableformat.py`. Puedes hacer esto ejecutando los siguientes comandos en tu terminal. El comando `cd` cambia el directorio a la carpeta de tu proyecto, y el comando `code` abre el archivo `tableformat.py` en tu editor de código.

```bash
cd ~/project
code tableformat.py
```

Una vez abierto el archivo, encuentra la función `create_formatter()`. Actualmente, se ve así:

```python
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

Esta función toma un nombre como argumento y devuelve el formateador correspondiente. Pero queremos hacerla más flexible. Vamos a modificarla para que pueda aceptar argumentos opcionales para nuestros mixins.

Reemplaza la función `create_formatter()` existente con la versión mejorada que se muestra a continuación. Esta nueva función te permite especificar formatos de columna y si se deben convertir los encabezados a mayúsculas.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

Esta función mejorada funciona primero determinando la clase base del formateador en función del argumento `name`. Luego, dependiendo de si se proporcionan `column_formats` y `upper_headers`, crea una clase de formateador personalizada que incluye los mixins adecuados. Finalmente, devuelve una instancia de la clase de formateador personalizada.

Ahora, probemos nuestra función mejorada con diferentes combinaciones de opciones.

Primero, probemos el uso del formateo de columnas. Ejecuta el siguiente comando en tu terminal. Este comando importa las funciones y datos necesarios del archivo `tableformat.py`, crea un formateador con formateo de columnas y luego imprime una tabla utilizando ese formateador.

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Deberías ver la tabla con columnas formateadas. La salida se verá así:

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

A continuación, probemos el uso de encabezados en mayúsculas. Ejecuta el siguiente comando:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Deberías ver la tabla con encabezados en mayúsculas. La salida será:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Finalmente, combinemos ambas opciones. Ejecuta este comando:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Esto debería mostrar una tabla con columnas formateadas y encabezados en mayúsculas. La salida será:

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

La función mejorada también funciona con otros tipos de formateadores. Por ejemplo, probémoslo con el formateador CSV. Ejecuta el siguiente comando:

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Esto debería producir una salida CSV con columnas formateadas. La salida será:

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

Al mejorar la función `create_formatter()`, hemos creado una API amigable para los usuarios. Ahora, los usuarios pueden utilizar fácilmente los mixins sin tener que entender los detalles complejos de la herencia múltiple. Esto les da la flexibilidad de personalizar los formateadores según sus necesidades.
