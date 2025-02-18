# Не-вложенная кросс-валидация

Мы используем не-вложенную кросс-валидацию (Non-Nested Cross-Validation), чтобы настроить гиперпараметры и оценить производительность модели. Функция `GridSearchCV` выполняет полный поиск по заданным значениям параметров для оценщика (estimator). Мы используем 4-кратную кросс-валидацию.

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
