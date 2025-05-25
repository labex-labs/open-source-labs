# 하이퍼파라미터 튜닝

이 단계에서는 GridSearchCV 를 사용하여 분류기의 하이퍼파라미터를 튜닝합니다.

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
