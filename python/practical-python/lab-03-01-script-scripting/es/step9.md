# Cadenas de documentación

Es una buena práctica incluir documentación en forma de una cadena de documentación (doc-string). Las cadenas de documentación son cadenas escritas inmediatamente después del nombre de la función. Son utilizadas por `help()`, entornos de desarrollo integrados (IDEs) y otras herramientas.

```python
def read_prices(filename):
    '''
    Lee los precios de un archivo CSV con datos de nombre,precio
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Una buena práctica para las cadenas de documentación es escribir un resumen corto en una sola oración de lo que hace la función. Si se necesita más información, incluir un ejemplo corto de uso junto con una descripción más detallada de los argumentos.
