# Ejercicio 4.4: Usando tu clase

Modifica la función `read_portfolio()` en el programa `report.py` de modo que lea una cartera en una lista de instancias de `Stock` como se mostró en el Ejercicio 4.3. Una vez que hayas hecho eso, corrige todo el código en `report.py` y `pcost.py` para que funcione con instancias de `Stock` en lugar de diccionarios.

Pista: No deberías tener que hacer cambios importantes en el código. Principalmente estarás cambiando el acceso a los diccionarios como `s['shares']` a `s.shares`.

Deberías poder ejecutar tus funciones como antes:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
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
