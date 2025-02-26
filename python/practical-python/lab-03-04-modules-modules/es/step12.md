# Ejercicio 3.11: Importaciones de módulos

En la sección 3, creamos una función general `parse_csv()` para analizar el contenido de archivos de datos CSV.

Ahora, vamos a ver cómo usar esa función en otros programas. Primero, comienza en una nueva ventana de shell. Navega hasta la carpeta donde tienes todos tus archivos. Vamos a importarlos.

Inicia el modo interactivo de Python.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, 21 mar 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] en darwin
Escribe "help", "copyright", "credits" o "license" para más información.
>>>
```

Una vez que hayas hecho eso, intenta importar algunos de los programas que escribiste anteriormente. Deberías ver su salida exactamente como antes. Solo para enfatizar, importar un módulo ejecuta su código.

```python
>>> import bounce
... observa la salida...
>>> import mortgage
... observa la salida...
>>> import report
... observa la salida...
>>>
```

Si nada de esto funciona, es probable que estés ejecutando Python en el directorio incorrecto. Ahora, intenta importar tu módulo `fileparse` y obtener ayuda sobre él.

```python
>>> import fileparse
>>> help(fileparse)
... mira la salida...
>>> dir(fileparse)
... mira la salida...
>>>
```

Intenta usar el módulo para leer algunos datos:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... mira la salida...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... mira la salida...
>>> prices = dict(pricelist)
>>> prices
... mira la salida...
>>> prices['IBM']
106.28
>>>
```

Intenta importar una función para que no tengas que incluir el nombre del módulo:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... mira la salida...
>>>
```
