# Test de permutation du score sur les données originales

Ensuite, nous calculons le `permutation_test_score` en utilisant le jeu de données iris original et le classifieur `SVC` avec le score `accuracy` pour évaluer le modèle à chaque itération.

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
