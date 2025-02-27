# Définir l'estimateur et la stratégie d'arrêt précoce

La prochaine étape consiste à définir l'estimateur et la stratégie d'arrêt précoce. Nous utiliserons le modèle `SGDClassifier` de scikit-learn. Nous définirons trois critères d'arrêt différents : aucun critère d'arrêt, perte d'entraînement et score de validation. Nous utiliserons la fonction `fit_and_score` pour ajuster l'estimateur sur l'ensemble d'entraînement et le noter sur les deux ensembles.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """Ajuster l'estimateur sur l'ensemble d'entraînement et le noter sur les deux ensembles"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# Définir l'estimateur à comparer
estimator_dict = {
    "Aucun critère d'arrêt": linear_model.SGDClassifier(n_iter_no_change=3),
    "Perte d'entraînement": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "Score de validation": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
