# Ejercicio 4.9: Mejor salida para la impresión de objetos

Modifica el objeto `Stock` que definiste en `stock.py` de modo que el método `__repr__()` produzca una salida más útil. Por ejemplo:

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Observa lo que sucede cuando lees una cartera de acciones y visualizas la lista resultante después de haber hecho estos cambios. Por ejemplo:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... ver cuál es la salida...
>>>
```
