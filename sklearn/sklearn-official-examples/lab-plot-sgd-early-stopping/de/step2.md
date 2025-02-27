# Definiere den Schätzer und die Early-Stopping-Strategie

Der nächste Schritt besteht darin, den Schätzer und die Early-Stopping-Strategie zu definieren. Wir werden das `SGDClassifier`-Modell aus scikit-learn verwenden. Wir werden drei verschiedene Stoppkriterien definieren: Kein Stoppkriterium, Trainingsverlust und Validierungsscore. Wir werden die `fit_and_score`-Funktion verwenden, um den Schätzer auf dem Trainingssatz anzupassen und ihn auf beiden Sätzen zu bewerten.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """Passe den Schätzer auf dem Trainingssatz an und bewerte ihn auf beiden Sätzen"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# Definiere den Schätzer zum Vergleich
estimator_dict = {
    "Kein Stoppkriterium": linear_model.SGDClassifier(n_iter_no_change=3),
    "Trainingsverlust": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "Validierungsscore": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
