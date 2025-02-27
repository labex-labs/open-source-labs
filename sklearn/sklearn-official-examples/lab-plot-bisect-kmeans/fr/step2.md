# Générer des données d'échantillonnage

Dans cette étape, nous allons générer des données d'échantillonnage à l'aide de la fonction `make_blobs()` de scikit-learn. Nous allons générer 10 000 échantillons avec 2 centres.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
