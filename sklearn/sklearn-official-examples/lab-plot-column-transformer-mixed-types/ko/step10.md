# 하이퍼파라미터 튜닝을 위한 그리드 서치 사용

이 단계에서는 그리드 서치를 사용하여 파이프라인의 하이퍼파라미터를 튜닝합니다.

```python
param_grid = {
    "preprocessor__num__imputer__strategy": ["mean", "median"],
    "preprocessor__cat__selector__percentile": [10, 30, 50, 70],
    "classifier__C": [0.1, 1.0, 10, 100],
}

search_cv = RandomizedSearchCV(clf, param_grid, n_iter=10, random_state=0)
search_cv.fit(X_train, y_train)

print("Best params:")
print(search_cv.best_params_)
print(f"Internal CV score: {search_cv.best_score_:.3f}")
```
