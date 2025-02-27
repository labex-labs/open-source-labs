# Prueba de permutación de puntuación en datos aleatorios

A continuación, calculamos la `permutación_test_score` utilizando las características generadas aleatoriamente y las etiquetas de iris, que no deben tener dependencia entre las características y las etiquetas.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
