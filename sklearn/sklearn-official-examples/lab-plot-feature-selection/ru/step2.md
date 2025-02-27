# Отбор признаков в задачах с одним признаком

Далее мы выполним отбор признаков в задачах с одним признаком с использованием F-теста для оценки значимости признаков. Мы будем использовать функцию выбора по умолчанию для выбора четырех наиболее значимых признаков.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
