# Ajuster un modèle mixte gaussien avec l'EM

Nous allons ajuster un modèle mixte gaussien classique avec 10 composantes en utilisant l'algorithme d'espérance-maximisation.

```python
# Ajuster un mélange gaussien avec l'EM en utilisant dix composantes
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
