# Générer des données d'entraînement

Dans cette étape, nous allons générer quelques données d'entraînement à partir de la classification. Nous utiliserons la fonction `make_blobs` de scikit-learn pour générer 5000 échantillons avec 3 clusters ayant des écarts-types et des centres différents.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
