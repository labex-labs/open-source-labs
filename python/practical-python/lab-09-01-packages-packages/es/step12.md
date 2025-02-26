# Ejercicio 9.2: Crear un directorio de aplicación

Poner todo tu código en un "paquete" no es a menudo suficiente para una aplicación. A veces hay archivos de soporte, documentación, scripts y otras cosas. Estos archivos deben existir FUERA del directorio `porty/` que creaste anteriormente.

Crea un nuevo directorio llamado `porty-app`. Mueve el directorio `porty` que creaste en el Ejercicio 9.1 a ese directorio. Copia los archivos de prueba `portfolio.csv` y `prices.csv` en este directorio. Además, crea un archivo `README.txt` con información sobre ti mismo. Tu código ahora debería estar organizado como sigue:

    porty-app/
        portfolio.csv
        prices.csv
        README.txt
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

Para ejecutar tu código, debes asegurarte de trabajar en el directorio principal `porty-app/`. Por ejemplo, desde la terminal:

```python
$ cd porty-app
$ python3
>>> import porty.report
>>>
```

Intenta ejecutar algunos de tus scripts anteriores como un programa principal:

```python
$ cd porty-app
$ python3 -m porty.report portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

$
```
