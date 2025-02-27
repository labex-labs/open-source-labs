# Générer de nouveaux échantillons

Dans cette étape, nous allons générer de nouveaux échantillons et les tracer avec l'ensemble de données d'origine. Nous utiliserons à nouveau la fonction `make_blobs` pour générer 10 nouveaux échantillons.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```
