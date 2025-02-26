# Ejercicio 3.15: Funciones `main()`

En el archivo `report.py` agregue una función `main()` que acepte una lista de opciones de línea de comandos y produzca la misma salida que antes. Debería poder ejecutarlo de manera interactiva como esto:

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Modifique el archivo `pcost.py` de modo que tenga una función `main()` similar:

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
