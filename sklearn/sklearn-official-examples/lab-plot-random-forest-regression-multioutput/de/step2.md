# Erstellen eines zufälligen Datensatzes

Als nächstes werden wir einen zufälligen Datensatz erstellen, den wir für unsere Regression verwenden. Wir werden `numpy` verwenden, um einen Satz von 600 x-Werten zwischen -100 und 100 zu erstellen und die entsprechenden y-Werte, die aus der Sinus- und Kosinusfunktion der x-Werte plus etwas zufälligem Rauschen berechnet werden.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
