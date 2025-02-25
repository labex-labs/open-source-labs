# Generieren von Beispielsdaten

Als nächstes werden wir einige Beispielsdaten generieren, die wir für das Histogramm verwenden. In diesem Beispiel werden wir drei Mengen von Zufallsdaten generieren.

```python
np.random.seed(19680801)
n_bins = 10
x = np.random.randn(1000, 3)
```
