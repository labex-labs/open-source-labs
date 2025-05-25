# 교차 검증을 이용한 최적 반복 횟수 추정

교차 검증을 사용하여 최적의 반복 횟수를 추정할 수 있습니다. 5-겹 교차 검증을 사용하고 각 반복 횟수에 대한 음수 로그 손실을 계산합니다.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
