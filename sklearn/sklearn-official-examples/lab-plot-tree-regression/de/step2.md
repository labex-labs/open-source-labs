# Erzeuge einen zufälligen Datensatz

Wir werden einen zufälligen Datensatz mit NumPy erstellen und ihm etwas Rauschen hinzufügen.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
