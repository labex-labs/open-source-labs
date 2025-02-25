# Daten generieren

Wir generieren einige Beispiel-Daten zum Plotten, indem wir die `mgrid`-Funktion von `numpy` verwenden.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
