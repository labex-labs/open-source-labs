# 교차 검증 수행 및 결과 기록

각 C 값에 대해 10 겹 교차 검증을 수행하고 점수의 평균과 표준 편차를 기록합니다.

```python
from sklearn.model_selection import cross_val_score

scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, X, y, n_jobs=1)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))
```
