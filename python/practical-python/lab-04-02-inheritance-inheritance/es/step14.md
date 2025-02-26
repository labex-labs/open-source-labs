# Ejercicio 4.7: El polimorfismo en acción

Una característica principal de la programación orientada a objetos es que puedes insertar un objeto en un programa y funcionará sin necesidad de cambiar ningún código existente. Por ejemplo, si escribes un programa que espera utilizar un objeto `TableFormatter`, funcionará sin importar de qué tipo de `TableFormatter` se le proporcione en realidad. Este comportamiento a veces se conoce como "polimorfismo".

Un problema potencial es determinar cómo permitir que el usuario elija el formateador que desea. El uso directo de los nombres de clase como `TextTableFormatter` a menudo es molesto. Por lo tanto, es posible que consideres un enfoque simplificado. Tal vez insertes una instrucción `if` en el código como esta:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Hace un informe de acciones a partir de archivos de datos de cartera y precios.
    '''
    # Lee los archivos de datos
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Crea los datos del informe
    report = make_report_data(portfolio, prices)

    # Imprime los datos
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Formato desconocido {fmt}')
    print_report(report, formatter)
```

En este código, el usuario especifica un nombre simplificado como `'txt'` o `'csv'` para elegir un formato. Sin embargo, ¿es poner una gran instrucción `if` en la función `portfolio_report()` de esa manera la mejor idea? Tal vez sea mejor mover ese código a una función de uso general en otro lugar.

En el archivo `tableformat.py`, agrega una función `create_formatter(name)` que permita a un usuario crear un formateador dado un nombre de salida como `'txt'`, `'csv'` o `'html'`. Modifica `portfolio_report()` de modo que se vea así:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Hace un informe de acciones a partir de archivos de datos de cartera y precios.
    '''
    # Lee los archivos de datos
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Crea los datos del informe
    report = make_report_data(portfolio, prices)

    # Imprime los datos
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Intenta llamar a la función con diferentes formatos para asegurarte de que funcione.
