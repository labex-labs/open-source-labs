# Ejercicio 4.8: Combinando todo

Modifica el programa `report.py` de modo que la función `portfolio_report()` tome un argumento opcional que especifique el formato de salida. Por ejemplo:

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
      Nombre     Acciones      Precio     Cambio
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

Modifica el programa principal para que se pueda especificar un formato en la línea de comandos:

```bash
$ python3 report.py portfolio.csv prices.csv csv
Nombre,Acciones,Precio,Cambio
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```
