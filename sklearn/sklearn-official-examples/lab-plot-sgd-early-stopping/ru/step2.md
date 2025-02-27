# Определение оценщика и стратегии ранней остановки

Следующим шагом является определение оценщика и стратегии ранней остановки. Мы будем использовать модель `SGDClassifier` из scikit-learn. Мы определим три различных критерия остановки: отсутствие критерия остановки, потеря на обучении и валидационный показатель. Мы будем использовать функцию `fit_and_score`, чтобы подогнать оценщик на обучающем наборе и оценить его на обоих наборах.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """Подгоняет оценщик на обучающем наборе и оценивает его на обоих наборах"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# Определение оценщика для сравнения
estimator_dict = {
    "Без критерия остановки": linear_model.SGDClassifier(n_iter_no_change=3),
    "Потеря на обучении": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "Валидационный показатель": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
