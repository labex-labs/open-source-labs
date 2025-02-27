# Datensatz laden

Wir werden den Kalifornien-Hauspreis-Datensatz von Scikit-Learn laden. Wir werden nur 2.000 Stichproben verwenden, um die Rechenzeit zu reduzieren.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
