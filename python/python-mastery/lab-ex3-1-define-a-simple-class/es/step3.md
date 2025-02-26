# Imprimiendo una Tabla

Tabla los datos leídos en el paso 2 y úsalo para crear una tabla con un formato agradable. Por ejemplo:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Toma este código y ponlo en una función `print_portfolio()` que produzca la misma salida, pero además agregue algunos encabezados de tabla. Por ejemplo:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

## Nota:

Completa la función `print_portfolio()` en el archivo `stock.py`.
