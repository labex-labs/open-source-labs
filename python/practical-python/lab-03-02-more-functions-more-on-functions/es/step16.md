# Ejercicio 3.6: Trabajar sin encabezados

Algunos archivos CSV no incluyen ninguna información de encabezado. Por ejemplo, el archivo `prices.csv` se ve así:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modifica la función `parse_csv()` en `/home/labex/project/fileparse_3.6.py` para que pueda trabajar con tales archivos creando una lista de tuplas en lugar de eso. Por ejemplo:

```python
>>> prices = parse_csv('/home/labex/project/prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

Para hacer este cambio, necesitarás modificar el código para que la primera línea de datos no se interprete como una línea de encabezado. Además, necesitarás asegurarte de no crear diccionarios ya que ya no hay nombres de columna para usar como claves.
