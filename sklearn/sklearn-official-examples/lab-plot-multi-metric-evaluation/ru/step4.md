# Выполняем сеточный поиск

В этом шаге мы будем использовать функцию GridSearchCV для выполнения сеточного поиска. Мы будем искать наилучшие гиперпараметры для параметра min_samples_split модели DecisionTreeClassifier.

```python
gs = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"min_samples_split": range(2, 403, 20)},
    scoring=scoring,
    refit="AUC",
    n_jobs=2,
    return_train_score=True,
)
gs.fit(X, y)
results = gs.cv_results_
```
