# Тест перестановочной оценки на исходных данных

Далее мы вычисляем `permutation_test_score` с использованием исходного набора данных iris и классификатора `SVC` с оценкой `accuracy`, чтобы оценить модель на каждой итерации.

```python
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import permutation_test_score

clf = SVC(kernel="linear", random_state=7)
cv = StratifiedKFold(2, shuffle=True, random_state=0)

score_iris, perm_scores_iris, pvalue_iris = permutation_test_score(
    clf, X, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
