# Interfaces y verificación de tipos

Modifica la función `print_table()` para que verifique si la instancia de formateador suministrada hereda de `TableFormatter`. Si no es así, lanza un `TypeError`.

Tu nuevo código debería capturar situaciones como esta:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

Agregar una verificación como esta podría agregar cierto grado de seguridad al programa. Sin embargo, debes seguir siendo consciente de que la verificación de tipos es bastante débil en Python. No hay garantía de que el objeto pasado como formateador funcione correctamente incluso si resulta que hereda de la clase base adecuada. La siguiente parte aborda ese problema.
