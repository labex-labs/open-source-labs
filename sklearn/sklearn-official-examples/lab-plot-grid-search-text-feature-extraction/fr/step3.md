# Ajustement d'hyperparamètres

Nous utilisons RandomizedSearchCV pour explorer la grille d'hyperparamètres et trouver la meilleure combinaison d'hyperparamètres pour le pipeline. Dans ce cas, nous définissons n_iter = 40 pour limiter l'espace de recherche. Nous pouvons augmenter n_iter pour obtenir une analyse plus informative, mais cela augmentera le temps de calcul.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Effectuer une recherche sur grille...")
print("Hyperparamètres à évaluer :")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```
