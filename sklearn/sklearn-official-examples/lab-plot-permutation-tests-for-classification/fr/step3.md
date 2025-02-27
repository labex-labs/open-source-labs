# Test de permutation du score sur les données aléatoires

Ensuite, nous calculons le `permutation_test_score` en utilisant les fonctionnalités générées aléatoirement et les étiquettes iris, qui ne devraient pas avoir de dépendance entre les fonctionnalités et les étiquettes.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
