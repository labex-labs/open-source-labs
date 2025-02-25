# Generieren von Testdatenpunkten

Wir generieren eine Menge zufälliger Testdatenpunkte mit x- und y-Werten zwischen -1 und 1. Wir generieren auch eine entsprechende Menge von z-Werten, indem wir die in Schritt 2 definierte `experiment_res`-Funktion verwenden.

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
