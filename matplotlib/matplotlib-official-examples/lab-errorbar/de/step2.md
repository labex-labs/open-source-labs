# Beispiel-Daten erstellen

Als nächstes werden wir Beispiel-Daten erstellen, die wir im Diagramm verwenden. In diesem Beispiel werden wir die `numpy.arange()`-Funktion verwenden, um ein Array von Werten zwischen 0,1 und 4 mit einem Schritt von 0,5 zu erstellen. Anschließend werden wir die `numpy.exp()`-Funktion verwenden, um die Exponentialfunktion jedes Werts im Array zu berechnen.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
