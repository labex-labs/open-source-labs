# Ejercicio 9.1: Crear un paquete simple

Crea un directorio llamado `porty/` y coloca todos los archivos de Python anteriores en él. Además, crea un archivo `__init__.py` vacío y colócalo en el directorio. Deberías tener un directorio de archivos como este:

    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py

Elimina el archivo `__pycache__` que se encuentra en tu directorio. Este contiene módulos de Python pre-compilados de antes. Queremos comenzar de nuevo.

Intenta importar algunos de los módulos del paquete:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

Si estas importaciones fallan, ve al archivo apropiado y corrige las importaciones de módulos para incluir una importación relativa al paquete. Por ejemplo, una declaración como `import fileparse` podría cambiar a la siguiente:

    # report.py
    from. import fileparse

...

Si tienes una declaración como `from fileparse import parse_csv`, cambia el código a lo siguiente:

    # report.py
    from.fileparse import parse_csv

...
