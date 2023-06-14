# Permutation Test Score on Random Data

Next, we calculate the `permutation_test_score` using the randomly generated features and iris labels, which should have no dependency between features and labels.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```


