# Daten vorbereiten

In diesem Schritt werden wir die synthetischen Klassifikationsdatensätze für die Feature-Diskretisierung vorbereiten. Wir werden die scikit-learn-Bibliothek verwenden, um drei verschiedene Datensätze zu generieren: Monde, konzentrische Kreise und linear trennbare Daten.

```python
h = 0.02  # Schrittweite im Gitter

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
