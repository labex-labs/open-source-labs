# Verwendung des `import`-Statements

In früheren Übungen haben Sie zwei Programme `pcost.py` und `stock.py` geschrieben. Verwenden Sie das `import`-Statement, um diese Programme zu laden und ihre Funktionalität zu nutzen:

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

Wenn Sie die obigen Anweisungen nicht zum Laufen bringen können, haben Sie vielleicht Ihre Programme in einem komischen Verzeichnis platziert. Stellen Sie sicher, dass Sie Python im gleichen Verzeichnis wie Ihre Dateien ausführen oder dass das Verzeichnis in `sys.path` enthalten ist.
