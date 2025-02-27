# Ajuster les hyperparamètres

Dans cette étape, nous allons ajuster les hyperparamètres du classifieur à l'aide de GridSearchCV.

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
