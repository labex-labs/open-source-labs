# Agregar comprobación de tipos a print_table()

En este paso, vamos a mejorar la función `print_table()` en el archivo `tableformat.py`. Agregaremos una comprobación para verificar si el parámetro `formatter` es una instancia válida de `TableFormatter`. ¿Por qué necesitamos esto? Bueno, la comprobación de tipos es como una red de seguridad para tu código. Ayuda a asegurarse de que los datos con los que estás trabajando son del tipo correcto, lo que puede prevenir muchos errores difíciles de encontrar.

## Comprender la comprobación de tipos en Python

La comprobación de tipos es una técnica realmente útil en la programación. Te permite detectar errores temprano en el proceso de desarrollo. En Python, a menudo trabajamos con diferentes tipos de objetos, y a veces esperamos que se pase un cierto tipo de objeto a una función. Para comprobar si un objeto es de un tipo específico o una subclase de él, podemos usar la función `isinstance()`. Por ejemplo, si tienes una función que espera una lista, puedes usar `isinstance()` para asegurarte de que la entrada es realmente una lista.

## Modificar la función print_table()

Primero, abre el archivo `tableformat.py` en tu editor de código. Desplázate hacia abajo hasta el final del archivo, y encontrarás la función `print_table()`. Así es como se ve inicialmente:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

Esta función recibe algunos datos, una lista de columnas y un formateador. Luego, utiliza el formateador para imprimir una tabla. Pero en este momento, no comprueba si el formateador es del tipo correcto.

Vamos a modificarla para agregar la comprobación de tipos. Usaremos la función `isinstance()` para comprobar si el parámetro `formatter` es una instancia de `TableFormatter`. Si no lo es, lanzaremos un `TypeError` con un mensaje claro. Aquí está el código modificado:

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## Probar la implementación de la comprobación de tipos

Ahora que hemos agregado la comprobación de tipos, necesitamos asegurarnos de que funcione. Vamos a crear un nuevo archivo Python llamado `test_tableformat.py`. Aquí está el código que debes poner en él:

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

En este código, primero leemos algunos datos de cartera. Luego definimos una nueva clase de formateador llamada `MyFormatter` que no hereda de `TableFormatter`. Intentamos usar este formateador no compatible en la función `print_table()`. Si nuestra comprobación de tipos está funcionando, debería lanzar un `TypeError`.

Para ejecutar la prueba, abre tu terminal y navega hasta el directorio donde se encuentra el archivo `test_tableformat.py`. Luego ejecuta el siguiente comando:

```bash
python test_tableformat.py
```

Si todo está funcionando correctamente, deberías ver una salida como esta:

```
Test passed - caught error: Expected a TableFormatter
```

Esta salida confirma que nuestra comprobación de tipos está funcionando como se esperaba. Ahora, la función `print_table()` solo aceptará un formateador que sea una instancia de `TableFormatter` o una de sus subclases.
