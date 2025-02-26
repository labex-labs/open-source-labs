# Ejercicio 7.4: Pasar argumentos sin modificar

La función `fileparse.parse_csv()` tiene algunas opciones para cambiar el delimitador del archivo y para el informe de errores. Tal vez desees exponer esas opciones a la función `read_portfolio()` anterior. Haz este cambio:

    def read_portfolio(filename, **opts):
        '''
        Lee un archivo de cartera de acciones en una lista de diccionarios con claves
        name, shares y price.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

Una vez que hayas hecho el cambio, intenta leer un archivo con algunos errores:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

Ahora, intenta silenciar los errores:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
