# Beispiel-Daten generieren

Wir werden die Funktion `make_blobs` der scikit-learn-Bibliothek verwenden, um Beispiel-Daten zu generieren. Diese Funktion erzeugt isotrope Gaussian-Blobs für die Gruppierung. Wir werden 4000 Proben mit 4 Zentren generieren.

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
