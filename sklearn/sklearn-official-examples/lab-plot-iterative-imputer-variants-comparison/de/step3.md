# Fehlende Werte hinzufügen

Wir werden jedem Datensatz eine einzige fehlende Zahl hinzufügen.

```python
X_missing = X_full.copy()
y_missing = y_full
missing_samples = np.arange(n_samples)
missing_features = rng.choice(n_features, n_samples, replace=True)
X_missing[missing_samples, missing_features] = np.nan
```
