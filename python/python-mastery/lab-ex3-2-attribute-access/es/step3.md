# Creando un formateador de tablas utilizando el acceso a atributos

En programación, el acceso a atributos es un concepto fundamental que nos permite interactuar con las propiedades de los objetos. Ahora, vamos a poner en práctica lo que hemos aprendido sobre el acceso a atributos. Crearemos una utilidad útil: un formateador de tablas. Este formateador tomará una colección de objetos y los mostrará en un formato tabular, lo que hará que los datos sean más fáciles de leer y entender.

## Creando el módulo tableformat.py

Primero, necesitamos crear un nuevo archivo de Python. Este archivo contendrá el código para nuestro formateador de tablas.

Para crear el archivo, sigue estos pasos:

1. En el WebIDE, haz clic en el menú "File".
2. En el menú desplegable, selecciona "New File".
3. Guarda el archivo recién creado como `tableformat.py` en el directorio `/home/labex/project/`.

Ahora que tenemos nuestro archivo, escribamos el código para la función `print_table()` dentro de `tableformat.py`. Esta función se encargará de formatear e imprimir nuestros objetos en una tabla.

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

Analicemos lo que hace esta función:

1. Toma dos argumentos: una secuencia de objetos y una lista de nombres de atributos. La secuencia de objetos es los datos que queremos mostrar, y la lista de nombres de atributos le dice a la función qué propiedades de los objetos mostrar.
2. Imprime una fila de encabezado. La fila de encabezado contiene los nombres de los atributos que nos interesan.
3. Imprime una línea separadora. Esta línea ayuda a separar visualmente el encabezado de los datos.
4. Para cada objeto en la secuencia, imprime el valor de cada atributo especificado. Utiliza la función `getattr()` para acceder al valor del atributo de cada objeto.

Ahora, probemos nuestra función `print_table()` para ver si funciona como se espera.

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Cuando ejecutes el código anterior, deberías ver la siguiente salida:

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Una de las grandes ventajas de nuestra función `print_table()` es su flexibilidad. Podemos cambiar las columnas que se muestran simplemente cambiando la lista `fields`.

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

Ejecutar este código te dará la siguiente salida:

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

El poder de este enfoque radica en su generalidad. Podemos usar la misma función `print_table()` para imprimir tablas de cualquier tipo de objeto, siempre y cuando sepamos los nombres de los atributos que queremos mostrar. Esto hace que nuestro formateador de tablas sea una herramienta muy útil en nuestro conjunto de herramientas de programación.
