# Configurando una tubería de procesamiento

Una gran ventaja de los generadores es que te permiten crear programas que configuren tuberías de procesamiento, muy similar a las tuberías en los sistemas Unix. Experimenta con este concepto realizando estos pasos:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Bueno, eso es interesante. Lo que estás viendo aquí es que la salida de la función `follow()` se ha dirigido a la función `csv.reader()` y ahora estamos obteniendo una secuencia de filas divididas.
