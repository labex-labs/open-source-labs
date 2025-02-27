# 元のデータに対する順列検定スコア

次に、元のアヤメデータセットと `accuracy` スコアを持つ `SVC` 分類器を使用して、`permutation_test_score` を計算して、各ラウンドでモデルを評価します。

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
