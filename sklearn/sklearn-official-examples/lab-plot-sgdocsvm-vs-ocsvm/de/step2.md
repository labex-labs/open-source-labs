# Daten generieren

Wir werden für dieses Lab einen Toy-Datensatz generieren. Wir werden 500 Trainingsbeispiele und 20 Testbeispiele generieren. Wir werden auch 20 abnorme Beispiele generieren.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# Generiere Trainingsdaten
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# Generiere einige regelmäßige neue Beobachtungen
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Generiere einige abnorme neue Beobachtungen
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
