# OOB 오류율 계산

각 분류기마다 `n_estimators` 값의 범위를 반복하며 분류기를 데이터셋에 맞춥니다. 각 `n_estimators` 값에 대한 OOB 오류율을 기록하고 `OrderedDict` 객체에 저장합니다.

```python
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

min_estimators = 15
max_estimators = 150

for label, clf in ensemble_clfs:
    for i in range(min_estimators, max_estimators + 1, 5):
        clf.set_params(n_estimators=i)
        clf.fit(X, y)

        oob_error = 1 - clf.oob_score_
        error_rate[label].append((i, oob_error))
```
