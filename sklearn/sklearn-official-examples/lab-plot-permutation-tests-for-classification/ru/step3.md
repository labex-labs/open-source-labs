# Тест перестановочной оценки на случайных данных

Далее мы вычисляем `permutation_test_score` с использованием случайно сгенерированных признаков и меток iris, между которыми не должно быть зависимости.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
