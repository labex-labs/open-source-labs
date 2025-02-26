# Ejercicio 3.7: Elegir un separador de columnas diferente

Aunque los archivos CSV son bastante comunes, también es posible que encuentres un archivo que use un separador de columnas diferente, como una tabulación o un espacio. Por ejemplo, el archivo `portfolio.dat` se ve así:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

La función `csv.reader()` permite especificar un separador de columnas diferente de la siguiente manera:

```python
rows = csv.reader(f, delimiter=' ')
```

Modifica tu función `parse_csv()` en `/home/labex/project/fileparse_3.7.py` para que también permita cambiar el separador.

Por ejemplo:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
