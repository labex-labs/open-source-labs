# Creando una Función Fábrica

Al utilizar la herencia, un desafío común es que los usuarios tienen que recordar los nombres de las clases de formateadores específicas. Esto puede ser bastante molesto, especialmente a medida que aumenta el número de clases. Para simplificar este proceso, podemos crear una función fábrica. Una función fábrica es un tipo especial de función que crea y devuelve objetos. En nuestro caso, devolverá el formateador adecuado basado en un nombre de formato simple.

Agreguemos la siguiente función a tu archivo `tableformat.py`. Esta función tomará un nombre de formato como argumento y devolverá el objeto formateador correspondiente.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

La función `create_formatter()` es una función fábrica. Verifica el argumento `format_name` que proporcionas. Si es 'text', crea y devuelve un objeto `TextTableFormatter`. Si es 'csv', devuelve un objeto `CSVTableFormatter`, y si es 'html', devuelve un objeto `HTMLTableFormatter`. Si el nombre de formato no es reconocido, genera una excepción `ValueError`. De esta manera, los usuarios pueden seleccionar fácilmente un formateador simplemente proporcionando un nombre simple, sin tener que conocer los nombres de las clases específicas.

Ahora, probemos la función fábrica. Usaremos algunas funciones y clases existentes para leer datos de un archivo CSV e imprimirlos en diferentes formatos.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

En este código, primero importamos los módulos y funciones necesarios. Luego leemos datos del archivo `portfolio.csv` y creamos un objeto `portfolio`. Después de eso, probamos la función `create_formatter()` con diferentes nombres de formato: 'text', 'csv' y 'html'. Para cada formato, creamos un objeto formateador, imprimimos el nombre del formato y luego usamos la función `print_table()` para imprimir los datos del `portfolio` en el formato especificado.

Cuando ejecutes este código, deberías ver la salida en los tres formatos, separados por el nombre del formato:

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

La función fábrica hace que el código sea más amigable para el usuario porque oculta los detalles de la instanciación de la clase. Los usuarios no necesitan saber cómo crear objetos formateadores; solo necesitan especificar el formato que desean.

Este patrón de usar una función fábrica para crear objetos es un patrón de diseño común en la programación orientada a objetos, conocido como el Patrón Fábrica. Proporciona una capa de abstracción entre el código cliente (el código que utiliza el formateador) y las clases de implementación reales (las clases de formateadores). Esto hace que el código sea más modular y fácil de usar.

**Revisión de Conceptos Clave:**

1. **Clase Base Abstracta**: La clase `TableFormatter` sirve como una interfaz. Una interfaz define un conjunto de métodos que todas las clases que la implementan deben tener. En nuestro caso, todas las clases de formateadores deben implementar los métodos definidos en la clase `TableFormatter`.

2. **Herencia**: Las clases de formateadores concretas, como `TextTableFormatter`, `CSVTableFormatter` y `HTMLTableFormatter`, heredan de la clase base `TableFormatter`. Esto significa que obtienen la estructura básica y los métodos de la clase base y pueden proporcionar sus propias implementaciones específicas.

3. **Polimorfismo**: La función `print_table()` puede trabajar con cualquier formateador que implemente la interfaz requerida. Esto significa que puedes pasar diferentes objetos formateadores a la función `print_table()`, y funcionará correctamente con cada uno.

4. **Patrón Fábrica**: La función `create_formatter()` simplifica la creación de objetos formateadores. Se encarga de los detalles de crear el objeto correcto basado en el nombre del formato, por lo que los usuarios no tienen que preocuparse por ello.

Al utilizar estos principios de programación orientada a objetos, hemos creado un sistema flexible y extensible para formatear datos tabulares en varios formatos de salida.
