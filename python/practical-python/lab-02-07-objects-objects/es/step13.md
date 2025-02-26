# Ejercicio 2.26: El panorama general

Utilizando las técnicas de este ejercicio, podrías escribir declaraciones que con facilidad conviertan los campos de casi cualquier archivo de datos orientado a columnas en un diccionario de Python.

Solo para ilustrar, supongamos que lees datos de un archivo de datos diferente de esta manera:

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

Vamos a convertir los campos usando un truco similar:

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

Bono: ¿Cómo modificarias este ejemplo para analizar adicionalmente la entrada `date` en una tupla como `(6, 11, 2007)`?

Tómate un tiempo para reflexionar sobre lo que has hecho en este ejercicio. Volveremos a estas ideas un poco más tarde.
