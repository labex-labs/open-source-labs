# Datensatz laden

Wir werden den Kalifornien-Hauspreis-Datensatz mit der Funktion `fetch_california_housing` aus scikit-learn laden. Dieser Datensatz besteht aus 20.640 Proben und 8 Merkmalen.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"Der Datensatz besteht aus {n_samples} Proben und {n_features} Merkmalen")
```
