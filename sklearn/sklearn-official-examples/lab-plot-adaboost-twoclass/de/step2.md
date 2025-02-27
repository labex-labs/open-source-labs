# Datensatz erstellen

In diesem Schritt erstellen wir einen nicht-linear trennbaren Klassifizierungsdatensatz, der aus zwei Gaussian Quantilen-Clustern besteht, mithilfe der Funktion `make_gaussian_quantiles` aus dem Modul `sklearn.datasets`. Wir verbinden auch die beiden Cluster und weisen ihnen Labels zu.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
