# Pontuação do Teste de Permutação nos Dados Originais

Em seguida, calculamos a `permutation_test_score` usando o conjunto de dados iris original e o classificador `SVC` com a pontuação `accuracy` para avaliar o modelo em cada rodada.

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
