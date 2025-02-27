# Выполнить кросс-валидацию и записать результаты

Для каждого значения C мы выполняем 10-кратную кросс-валидацию и записываем среднее значение и стандартное отклонение оценок.

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
