# Definieren von Daten

Als nächstes werden wir einige Beispiel-Daten definieren, um zu plotten. Hier werden wir ein Array von x-Werten, y-Werten und ihren entsprechenden Fehlerwerten erstellen.

```python
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y = np.exp(-x)
xerr = 0.1
yerr = 0.2
```
