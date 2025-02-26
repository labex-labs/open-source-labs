# Mirar asombrado

Intente ejecutar las pruebas unitarias de `teststock.py` en este nuevo archivo. La mayoría de ellas ahora deberían pasar. Por diversión, pruebe su clase `Stock` con algunos de los códigos anteriores para el formato de tabla y la lectura de datos. Todo debería funcionar.

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
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

Una vez más, admirá el archivo final `stock.py` y observará lo limpio que se ve el código. Simplemente intente no pensar en todo lo que está sucediendo por debajo del capó con la clase base `Structure`.
