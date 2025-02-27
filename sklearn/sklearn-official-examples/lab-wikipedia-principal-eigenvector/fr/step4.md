# Calcul du vecteur singulier principal à l'aide de la SVD aléatoire

Nous allons calculer les vecteurs singuliers principaux à l'aide de la méthode randomized_svd implémentée dans scikit-learn.

```python
from sklearn.decomposition import randomized_svd

print("Calcul des vecteurs singuliers principaux à l'aide de randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
