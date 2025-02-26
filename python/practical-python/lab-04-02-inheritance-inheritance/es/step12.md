# Ejercicio 4.5: Un problema de extensibilidad

Supongamos que quieres modificar la función `print_report()` para que soporte una variedad de formatos de salida diferentes, como texto plano, HTML, CSV o XML. Para hacer esto, podrías intentar escribir una función gigantesca que hiciera todo. Sin embargo, hacer eso probablemente llevaría a un desastre inmanejable. En cambio, esta es una oportunidad perfecta para usar la herencia en su lugar.

Para comenzar, centra en los pasos que se involucran en la creación de una tabla. En la parte superior de la tabla hay un conjunto de encabezados de tabla. Después de eso, aparecen filas de datos de tabla. Tomemos esos pasos y los pongamos en su propia clase. Crea un archivo llamado `tableformat.py` y define la siguiente clase:

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emite los encabezados de la tabla.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emite una sola fila de datos de tabla.
        '''
        raise NotImplementedError()
```

Esta clase no hace nada, pero sirve como una especie de especificación de diseño para clases adicionales que se definirán en breve. Una clase como esta a veces se llama "clase base abstracta".

Modifica la función `print_report()` de modo que acepte un objeto `TableFormatter` como entrada e invoque métodos en él para producir la salida. Por ejemplo, así:

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Imprime una tabla bien formateada a partir de una lista de tuplas (nombre, acciones, precio, cambio).
    '''
    formatter.headings(['Nombre','Acciones','Precio','Cambio'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Dado que agregaste un argumento a `print_report()`, también tendrás que modificar la función `portfolio_report()`. Cambiala de modo que cree un `TableFormatter` como este:

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    Hace un informe de acciones a partir de archivos de datos de cartera y precios.
    '''
    # Lee los archivos de datos
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Crea los datos del informe
    report = make_report_data(portfolio, prices)

    # Imprime los datos
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Ejecuta este nuevo código:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... se detiene con error...
```

Debería detenerse inmediatamente con una excepción `NotImplementedError`. Eso no es muy emocionante, pero es exactamente lo que esperábamos. Continúa con la siguiente parte.
