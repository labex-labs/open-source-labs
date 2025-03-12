# Creando Formateadores Adicionales

En programación, la herencia es un concepto poderoso que nos permite crear nuevas clases basadas en las existentes. Esto ayuda a reutilizar código y hacer nuestros programas más extensibles. En esta parte del experimento, usaremos la herencia para crear dos nuevos formateadores para diferentes formatos de salida: CSV y HTML. Estos formateadores heredarán de una clase base, lo que significa que compartirán cierto comportamiento común mientras tendrán sus propias maneras únicas de formatear datos.

Ahora, agreguemos las siguientes clases a tu archivo `tableformat.py`. Estas clases definirán cómo formatear datos en formatos CSV y HTML respectivamente.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

La clase `CSVTableFormatter` está diseñada para formatear datos en el formato CSV (Comma-Separated Values, Valores Separados por Comas). El método `headings` toma una lista de encabezados e imprime cada uno separado por comas. El método `row` toma una lista de datos para una sola fila y también los imprime separados por comas.

Por otro lado, la clase `HTMLTableFormatter` se utiliza para generar código de tabla HTML. El método `headings` crea los encabezados de la tabla utilizando etiquetas HTML `<th>`, y el método `row` crea una fila de la tabla utilizando etiquetas HTML `<td>`.

Probemos estos nuevos formateadores para ver cómo funcionan.

1. Primero, probemos el formateador CSV:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

En este código, primero importamos los módulos necesarios. Luego leemos datos de un archivo CSV llamado `portfolio.csv` y creamos instancias de la clase `Stock`. A continuación, creamos una instancia de la clase `CSVTableFormatter`. Finalmente, usamos la función `print_table` para imprimir los datos del portafolio en formato CSV.

Deberías ver la siguiente salida en formato CSV:

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Ahora probemos el formateador HTML:

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Aquí, creamos una instancia de la clase `HTMLTableFormatter` y usamos nuevamente la función `print_table` para imprimir los datos del portafolio en formato HTML.

Deberías ver la siguiente salida en formato HTML:

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Como puedes ver, cada formateador produce una salida en un formato diferente, pero todos comparten la misma interfaz definida por la clase base `TableFormatter`. Este es un gran ejemplo del poder de la herencia y el polimorfismo. Podemos escribir código que funcione con la clase base, y automáticamente funcionará con cualquier subclase.

La función `print_table()` no necesita saber nada sobre el formateador específico que se está utilizando. Simplemente llama a los métodos definidos en la clase base, y la implementación adecuada se selecciona según el tipo de formateador proporcionado. Esto hace que nuestro código sea más flexible y fácil de mantener.
