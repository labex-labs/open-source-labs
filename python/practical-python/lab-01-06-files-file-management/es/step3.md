# Expresiones habituales para escribir en un archivo

Escribir datos de cadena.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

Redirigir la función print.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

Estos ejercicios dependen de un archivo `portfolio.csv`. El archivo contiene una lista de líneas con información sobre un portafolio de acciones. Se asume que estás trabajando en el directorio `~/project/`. Si no estás seguro, puedes averiguar dónde Python cree que está ejecutándose haciendo lo siguiente:

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # Output vary
>>>
```
