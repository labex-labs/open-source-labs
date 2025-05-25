# Definir o estimador e a estratégia de parada antecipada

O próximo passo é definir o estimador e a estratégia de parada antecipada. Usaremos o modelo `SGDClassifier` do scikit-learn. Definiremos três critérios de parada diferentes: sem critério de parada, perda de treinamento e pontuação de validação. Usaremos a função `fit_and_score` para ajustar o estimador no conjunto de treinamento e avaliar no conjunto de treinamento e no conjunto de teste.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """Ajustar o estimador no conjunto de treinamento e avaliar no conjunto de treinamento e no conjunto de teste"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# Definir o estimador para comparação
estimator_dict = {
    "Sem critério de parada": linear_model.SGDClassifier(n_iter_no_change=3),
    "Perda de treinamento": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "Pontuação de validação": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
