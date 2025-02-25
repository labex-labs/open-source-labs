# Ejercicio 1.32: Usando una función de la biblioteca

Python viene con una gran biblioteca estándar de funciones útiles. Una biblioteca que podría ser útil aquí es el módulo `csv`. Debería usarlo siempre que tenga que trabajar con archivos de datos CSV. Aquí hay un ejemplo de cómo funciona:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

Una de las cosas buenas del módulo `csv` es que se ocupa de una variedad de detalles de bajo nivel, como la citación y la división correcta por comas. En la salida anterior, notará que ha quitado las comillas dobles de los nombres en la primera columna.

Modifique su programa `pcost.py` para que use el módulo `csv` para el análisis y pruebe a ejecutar los ejemplos anteriores.
