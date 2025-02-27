# Realizar la búsqueda en cuadrícula

En este paso, utilizaremos la función GridSearchCV para realizar la búsqueda en cuadrícula. Estaremos buscando los mejores hiperparámetros para el parámetro min_samples_split del modelo DecisionTreeClassifier.

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
