# 원본 데이터에 대한 퍼뮤테이션 테스트 점수

다음으로, 원본 붓꽃 데이터셋과 `SVC` 분류기, 그리고 각 라운드에서 모델을 평가하기 위한 `accuracy` 점수를 사용하여 `permutation_test_score`를 계산합니다.

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
