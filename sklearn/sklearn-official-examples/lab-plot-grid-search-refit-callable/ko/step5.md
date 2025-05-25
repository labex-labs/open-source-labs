# GridSearchCV 객체 정의

GridSearchCV 객체를 정의하고 모델을 학습시킵니다.

```python
grid = GridSearchCV(
    pipe,
    cv=10,
    n_jobs=1,
    param_grid=param_grid,
    scoring="accuracy",
    refit=best_low_complexity,
)

grid.fit(X, y)
```
