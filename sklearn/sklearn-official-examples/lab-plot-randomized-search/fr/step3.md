# Recherche aléatoire pour l'optimisation d'hyperparamètres

Nous utiliserons la recherche aléatoire pour explorer l'espace d'hyperparamètres et trouver les meilleurs hyperparamètres pour notre modèle SVM.

```python
# spécifiez les paramètres et les distributions à échantillonner
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# exécutez la recherche aléatoire
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV a pris %.2f secondes pour %d paramètres candidats."
    % ((time() - start), n_iter_search)
)

# affichez les résultats
report(random_search.cv_results_)
```
