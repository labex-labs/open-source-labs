# Tune Hyperparameters

In this step, we will tune the hyperparameters of the classifier using GridSearchCV.

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```


