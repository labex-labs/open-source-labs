# Daten generieren

In diesem Schritt generieren wir einen zufälligen Datensatz mit `n_samples` Proben und `n_features` Merkmalen. Wir fügen auch einige Ausreißer dem Datensatz hinzu.

```python
n_samples = 80
n_features = 5

# Generiere zufälligen Datensatz
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# Füge Ausreißer zum Datensatz hinzu
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
