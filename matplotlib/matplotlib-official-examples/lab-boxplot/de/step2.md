# Daten generieren

Wir werden einige zufällige Daten generieren, die wir in unseren Beispielen verwenden. Wir werden die NumPy-Funktion `random.lognormal()` verwenden, um log-normalverteilte Daten mit einem Mittelwert von 1,5 und einer Standardabweichung von 1,75 zu generieren. Wir werden 37 Proben von 4 Variablen generieren und sie in der Variable `data` speichern. Wir werden auch eine Liste von Bezeichnungen für jede Variable erstellen.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
