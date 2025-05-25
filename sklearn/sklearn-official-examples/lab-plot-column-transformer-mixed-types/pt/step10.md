# Usar Busca em Grade para Ajustar Hiperparâmetros

Neste passo, usaremos busca em grade para ajustar os hiperparâmetros do nosso pipeline.

```python
param_grid = {
    "preprocessor__num__imputer__strategy": ["mean", "median"],
    "preprocessor__cat__selector__percentile": [10, 30, 50, 70],
    "classifier__C": [0.1, 1.0, 10, 100],
}

search_cv = RandomizedSearchCV(clf, param_grid, n_iter=10, random_state=0)
search_cv.fit(X_train, y_train)

print("Melhores parâmetros:")
print(search_cv.best_params_)
print(f"Pontuação de validação cruzada interna: {search_cv.best_score_:.3f}")
```
