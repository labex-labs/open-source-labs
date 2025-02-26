# Pensando en Flexibilidad

En este momento, las dos funciones en `reader.py` están codificadas para trabajar con nombres de archivos que se pasan directamente a `open()`. Refactorice el código para que funcione con cualquier objeto iterable que produzca líneas. Para hacer esto, cree dos nuevas funciones `csv_as_dicts(lines, types)` y `csv_as_instances(lines, cls)` que conviertan cualquier secuencia iterable de líneas. Por ejemplo:

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

El objetivo principal de hacer esto es permitir trabajar con diferentes tipos de fuentes de entrada. Por ejemplo:

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

Para mantener la compatibilidad con versiones anteriores del código, escriba las funciones `read_csv_as_dicts()` y `read_csv_as_instances()` que tomen un nombre de archivo como antes. Estas funciones deben llamar a `open()` en el nombre de archivo suministrado y usar las nuevas funciones `csv_as_dicts()` o `csv_as_instances()` en el archivo resultante.
