# Ejercicio 4.10: Un ejemplo de uso de getattr()

`getattr()` es un mecanismo alternativo para leer atributos. Puede usarse para escribir código extremadamente flexible. Para comenzar, prueba este ejemplo:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name','shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

Observa detenidamente que los datos de salida se determinan enteramente por los nombres de atributos enumerados en la variable `columns`.

En el archivo `tableformat.py`, toma esta idea y amplíala en una función generalizada `print_table()` que imprima una tabla que muestra atributos especificados por el usuario de una lista de objetos arbitrarios. Al igual que la función `print_report()` anterior, `print_table()` también debe aceptar una instancia de `TableFormatter` para controlar el formato de salida. Aquí es cómo debería funcionar:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares', 'price'], formatter)
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
