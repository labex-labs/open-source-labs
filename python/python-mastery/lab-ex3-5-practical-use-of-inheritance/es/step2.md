# Creando una Clase Base y Modificando la Función de Impresión

En programación, la herencia es un concepto poderoso que nos permite crear una jerarquía de clases. Para comenzar a utilizar la herencia para mostrar datos en diferentes formatos, primero necesitamos crear una clase base. Una clase base sirve como un modelo para otras clases, definiendo un conjunto común de métodos que sus subclases pueden heredar y sobrescribir.

Ahora, creemos una clase base que definirá la interfaz para todos los formateadores de tablas. Abre el archivo `tableformat.py` en el WebIDE y agrega el siguiente código en la parte superior del archivo:

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

La clase `TableFormatter` es una clase base abstracta. Una clase base abstracta es una clase que define métodos pero no proporciona implementaciones para ellos. En lugar de eso, espera que sus subclases proporcionen estas implementaciones. Las excepciones `NotImplementedError` se utilizan para indicar que estos métodos deben ser sobrescritos por las subclases. Si una subclase no sobrescribe estos métodos y tratamos de utilizarlos, se generará un error.

A continuación, necesitamos modificar la función `print_table()` para utilizar la clase `TableFormatter`. La función `print_table()` se utiliza para imprimir una tabla de datos a partir de una lista de objetos. Al modificarla para que utilice la clase `TableFormatter`, podemos hacer que la función sea más flexible y capaz de trabajar con diferentes formatos de tabla.

Reemplaza la función `print_table()` existente con el siguiente código:

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

El cambio clave aquí es que `print_table()` ahora toma un parámetro `formatter`, que debe ser una instancia de `TableFormatter` o una subclase. Esto significa que podemos pasar diferentes formateadores de tablas a la función `print_table()`, y utilizará el formateador adecuado para imprimir la tabla. La función delega la responsabilidad de formateo al objeto formateador llamando a sus métodos `headings()` y `row()`.

Probemos nuestros cambios intentando utilizar la clase base `TableFormatter`:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Cuando ejecutes este código, deberías ver un error:

```
Traceback (most recent call last):
...
NotImplementedError
```

Este error se produce porque estamos tratando de utilizar directamente la clase base abstracta, pero no proporciona implementaciones para sus métodos. Dado que los métodos `headings()` y `row()` en la clase `TableFormatter` generan `NotImplementedError`, Python no sabe qué hacer cuando se llaman a estos métodos. En el siguiente paso, crearemos una subclase concreta que sí proporcione estas implementaciones.
