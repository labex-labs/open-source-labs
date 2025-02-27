# Définir une fonction pour obtenir les moyennes initiales

Ensuite, nous allons définir une fonction `get_initial_means` qui prend les données d'échantillonnage, la méthode d'initialisation et l'état aléatoire en entrée et renvoie les moyennes d'initialisation.

```python
def get_initial_means(X, init_params, r):
    # Exécutez un GaussianMixture avec max_iter=0 pour afficher les moyennes d'initialisation
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
