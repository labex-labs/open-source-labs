# Realizar a busca em grade

Nesta etapa, usaremos a função `GridSearchCV` para realizar a busca em grade. Iremos procurar os melhores hiperparâmetros para o parâmetro `min_samples_split` do modelo `DecisionTreeClassifier`.

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
