# 对原始数据进行排列检验分数计算

接下来，我们使用原始的鸢尾花数据集和带有“accuracy”分数的“SVC”分类器来计算“permutation_test_score”，以便在每一轮评估模型。

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
