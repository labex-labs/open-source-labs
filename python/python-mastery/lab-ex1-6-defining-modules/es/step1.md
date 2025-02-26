# Usando la declaración import

En ejercicios anteriores, escribió dos programas `pcost.py` y `stock.py`. Use la declaración `import` para cargar estos programas y usar su funcionalidad:

```python
>>> import pcost
44671.15
>>> pcost.portfolio_cost('portfolio2.dat')
19908.75
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Si no puede hacer que las declaraciones anteriores funcionen, es posible que haya colocado sus programas en un directorio extraño. Asegúrese de que está ejecutando Python en el mismo directorio que sus archivos o que el directorio se incluya en `sys.path`.
