# Übung 4.9: Bessere Ausgabe bei der Ausgabe von Objekten

Ändern Sie das `Stock`-Objekt, das Sie in `stock.py` definiert haben, so, dass die `__repr__()`-Methode eine nützlichere Ausgabe erzeugt. Beispielsweise:

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Sehen Sie sich an, was passiert, wenn Sie ein Portfolio von Aktien lesen und die resultierende Liste betrachten, nachdem Sie diese Änderungen vorgenommen haben. Beispielsweise:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... sehen Sie sich an, was die Ausgabe ist...
>>>
```
