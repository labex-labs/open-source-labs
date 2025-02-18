# Erstellen von Daten

Für dieses Beispiel werden wir einen zufälligen Datensatz mit `numpy.random.randn()` erstellen.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
