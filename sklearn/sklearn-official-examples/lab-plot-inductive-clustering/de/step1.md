# Trainingdaten generieren

In diesem Schritt werden wir einige Trainingdaten aus Clustering generieren. Wir werden die Funktion `make_blobs` aus scikit-learn verwenden, um 5000 Proben mit 3 Clustern zu generieren, die unterschiedliche Standardabweichungen und Zentren haben.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
