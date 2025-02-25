# ¿Por qué usar diccionarios?

Los diccionarios son útiles cuando hay _muchos_ valores diferentes y esos valores pueden ser modificados o manipulados. Los diccionarios hacen que su código sea más legible.

```python
s['price']
# vs
s[2]
```

En los últimos ejercicios, escribió un programa que lee un archivo de datos `portfolio.csv`. Usando el módulo `csv`, es fácil leer el archivo línea por línea.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name','shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Aunque leer el archivo es fácil, a menudo desea hacer más con los datos que solo leerlos. Por ejemplo, tal vez desee almacenarlos y comenzar a realizar algunos cálculos con ellos. Lamentablemente, una "fila" cruda de datos no le da suficiente información para trabajar. Por ejemplo, incluso un cálculo matemático simple no funciona:

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Para hacer más, generalmente desea interpretar los datos crudos de alguna manera y convertirlos en un tipo de objeto más útil para poder trabajar con ellos más adelante. Dos opciones simples son tuplas o diccionarios.
