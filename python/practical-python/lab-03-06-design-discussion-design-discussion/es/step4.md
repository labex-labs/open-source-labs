# Ejercicio 3.17: De nombres de archivos a objetos similares a archivos

Ahora has creado un archivo `fileparse.py` que contiene una función `parse_csv()`. La función funcionaba así:

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

En este momento, la función espera recibir un nombre de archivo. Sin embargo, puedes hacer que el código sea más flexible. Modifica la función para que funcione con cualquier objeto similar a un archivo/iterable. Por ejemplo:

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

En este nuevo código, ¿qué pasa si pasas un nombre de archivo como antes?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... mira la salida (debería ser un caos)...
>>>
```

Sí, tendrás que tener cuidado. ¿Podrías agregar una comprobación de seguridad para evitar esto?
