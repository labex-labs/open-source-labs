# Permutations-Test-Score auf zufälligen Daten

Als nächstes berechnen wir den `Permutations-Test-Score` mit den zufällig generierten Features und den Iris-Labels, zwischen denen es keine Abhängigkeit zwischen Features und Labels geben sollte.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
