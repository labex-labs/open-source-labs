# Un administrador de contexto

En el Ejercicio 3.5, hiciste posible que los usuarios crearan tablas bien formateadas. Por ejemplo:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Un problema con el código es que todas las tablas se imprimen en la salida estándar (`sys.stdout`). Supongamos que quisieras redirigir la salida a un archivo u otro destino. En general, podrías modificar todo el código de formato de tablas para permitir un archivo de salida diferente. Sin embargo, en un apuro, también podrías resolver esto con un administrador de contexto.

Define el siguiente administrador de contexto:

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

Este administrador de contexto funciona creando un parche temporal en `sys.stdout` para que toda la salida se redirija a un archivo diferente. Al salir, el parche se revierte. Prueba:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # Inspecciona el archivo
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
