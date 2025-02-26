# Preparación

En el Ejercicio 2.6 escribió un módulo `reader.py` que tenía una función para leer un archivo CSV en una lista de diccionarios. Por ejemplo:

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

Más tarde, expandimos ese código para trabajar con instancias en el Ejercicio 3.3:

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

Finalmente, el código se refactorizó en una colección de clases que involucra herencia en el Ejercicio 3.7. Sin embargo, el código se ha vuelto bastante complejo y complicado.
