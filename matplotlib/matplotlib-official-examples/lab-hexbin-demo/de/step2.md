# Daten generieren

Wir werden 100.000 Datenpunkte mit `numpy.random.standard_normal()` und `numpy.random.standard_normal()` generieren. `standard_normal()` generiert Zufallszahlen aus einer Standardnormalverteilung mit einem Mittelwert von 0 und einer Standardabweichung von 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
