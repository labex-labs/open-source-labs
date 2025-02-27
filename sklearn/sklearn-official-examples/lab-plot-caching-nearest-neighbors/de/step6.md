# Hyperparameter optimieren

In diesem Schritt werden wir die Hyperparameter des Klassifiziers mit GridSearchCV optimieren.

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
