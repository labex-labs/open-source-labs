# Salida en tabla

En el Ejercicio 3.1, escribió una función `print_portfolio()` que creaba una tabla con un formato agradable. Esa función estaba adaptada específicamente para una lista de objetos `Stock`. Sin embargo, se puede generalizar completamente para que funcione con cualquier lista de objetos utilizando la técnica del apartado (b).

Cree un nuevo módulo llamado `tableformat.py`. En ese programa, escriba una función `print_table()` que tome una secuencia (lista) de objetos, una lista de nombres de atributos y muestre una tabla con un formato agradable. Por ejemplo:

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

Para simplificar, que la función `print_table()` imprima cada campo en una columna de 10 caracteres de ancho.
