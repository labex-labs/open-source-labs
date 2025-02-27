# Оценка оптимального числа итераций с использованием кросс-валидации

Мы можем оценить оптимальное число итераций с использованием кросс-валидации. Мы будем использовать 5-кратную кросс-валидацию и вычислять отрицательный логарифмический лосс для каждого числа итераций.

```python
from sklearn.model_selection import cross_val_score

cv_scores = []
for i in range(1, params['n_estimators'] + 1):
    clf.set_params(n_estimators=i)
    scores = -1 * cross_val_score(clf, X, y, cv=5, scoring='neg_log_loss')
    cv_scores.append(scores.mean())
```
