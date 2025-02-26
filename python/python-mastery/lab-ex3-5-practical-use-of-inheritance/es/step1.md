# Preparación

Una de las principales usos de las clases en Python es escribir código que se pueda extender / adaptar de varias maneras. Para ilustrar, en el Ejercicio 3.2 creaste una función `print_table()` que creaba tablas. La usaste para generar la salida de la lista `portfolio`. Por ejemplo:

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
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
>>>
```

Supongamos que quisieras que la función `print_table()` fuera capaz de crear tablas en cualquier número de formatos de salida, como CSV, XML, HTML, Excel, etc. Intentar modificar la función para que soporte todos esos formatos de salida a la vez sería penoso. Una mejor manera de hacer esto implica mover el código de formato relacionado con la salida a una clase y usar la herencia para implementar diferentes formatos de salida.
