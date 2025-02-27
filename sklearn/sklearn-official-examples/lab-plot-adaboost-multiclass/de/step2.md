# Laden des Datensatzes

Wir werden die Funktion `make_gaussian_quantiles` aus `sklearn.datasets` verwenden, um einen Datensatz zu generieren. Diese Funktion erzeugt isotrope Gaussian-Verteilungen und fügt eine Trennung zwischen den Klassen hinzu, um das Problem schwieriger zu gestalten.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
