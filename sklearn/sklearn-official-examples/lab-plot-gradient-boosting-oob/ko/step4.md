# 테스트 데이터에 대한 최적 반복 횟수 계산

테스트 데이터에 대한 최적의 반복 횟수를 계산할 수도 있습니다. 테스트 데이터에서 각 반복 횟수에 대한 음수 로그 손실을 계산합니다.

```python
from sklearn.metrics import log_loss
import matplotlib.pyplot as plt

test_scores = []
for i, y_pred in enumerate(clf.staged_predict_proba(X)):
    score = log_loss(y, y_pred)
    test_scores.append(score)

best_n_estimators = np.argmin(test_scores) + 1
```
