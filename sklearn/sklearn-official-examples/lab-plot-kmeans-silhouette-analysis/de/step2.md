# Daten generieren

Wir werden Beispiel-Daten mit der Funktion `make_blobs` aus der Bibliothek `sklearn.datasets` generieren. Diese Funktion erzeugt isotrope Gaussian Blobs für Clustering.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
