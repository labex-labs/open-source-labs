# Ajustar Hiperparâmetros

Neste passo, ajustaremos os hiperparâmetros do classificador usando `GridSearchCV`.

```python
    param_grid = {"classifier__n_neighbors": n_neighbors_list}
    grid_model = GridSearchCV(full_model, param_grid)
    grid_model.fit(X, y)
```
