# Definir el estimador y la estrategia de parada temprana

El siguiente paso es definir el estimador y la estrategia de parada temprana. Utilizaremos el modelo `SGDClassifier` de scikit-learn. Definiremos tres criterios de parada diferentes: sin criterio de parada, pérdida de entrenamiento y puntuación de validación. Usaremos la función `fit_and_score` para ajustar el estimador en el conjunto de entrenamiento y evaluarlo en ambos conjuntos.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """Ajustar el estimador en el conjunto de entrenamiento y evaluarlo en ambos conjuntos"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# Definir el estimador para comparar
estimator_dict = {
    "Sin criterio de parada": linear_model.SGDClassifier(n_iter_no_change=3),
    "Pérdida de entrenamiento": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "Puntuación de validación": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
