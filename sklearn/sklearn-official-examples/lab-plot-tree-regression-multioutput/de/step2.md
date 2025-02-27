# Erstellen eines zufälligen Datensatzes

In diesem Schritt werden wir einen zufälligen Datensatz erstellen. Wir werden die `numpy`-Bibliothek verwenden, um einen sortierten Array mit 100 Elementen zu erstellen, mit zufälligen Werten von 0 bis 200, und anschließend wird von jedem Element 100 subtrahiert. Dann werden wir `numpy` verwenden, um die Sinus- und Kosinuswerte jedes Elements zu berechnen und diese Arrays zu einem 2D-Array der Form (100, 2) zusammenzufügen, um das `y`-Array zu erstellen. Wir werden auch jedem fünften Element zufälliges Rauschen hinzufügen.

```python
# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
