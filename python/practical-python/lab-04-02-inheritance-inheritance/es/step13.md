# Ejercicio 4.6: Usar la herencia para producir diferentes salidas

La clase `TableFormatter` que definiste en la parte (a) está destinada a ser extendida a través de la herencia. De hecho, esa es la idea principal. Para ilustrar, define una clase `TextTableFormatter` de la siguiente manera:

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Emite una tabla en formato de texto plano
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 +' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Modifica la función `portfolio_report()` de la siguiente manera y pruébalo:

```python
# report.py
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
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

Esto debería producir la misma salida que antes:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Nombre     Acciones      Precio     Cambio
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Sin embargo, cambiemos la salida a algo diferente. Define una nueva clase `CSVTableFormatter` que produce una salida en formato CSV:

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Salida de datos de cartera en formato CSV.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Modifica tu programa principal de la siguiente manera:

```python
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
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

Ahora deberías ver una salida CSV como esta:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Nombre,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

Usando una idea similar, define una clase `HTMLTableFormatter` que produce una tabla con la siguiente salida:

    <tr><th>Nombre</th><th>Acciones</th><th>Precio</th><th>Cambio</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

Prueba tu código modificando el programa principal para crear un objeto `HTMLTableFormatter` en lugar de un objeto `CSVTableFormatter`.
