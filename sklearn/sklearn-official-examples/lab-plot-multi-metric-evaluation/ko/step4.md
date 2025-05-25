# 그리드 검색 수행

이 단계에서는 `GridSearchCV` 함수를 사용하여 그리드 검색을 수행합니다. `DecisionTreeClassifier` 모델의 `min_samples_split` 매개변수에 대한 최적의 하이퍼파라미터를 찾을 것입니다.

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
