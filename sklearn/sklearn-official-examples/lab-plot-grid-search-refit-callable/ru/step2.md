# Определение функций

Мы определим две функции, которые будут использоваться позже в практическом занятии.

```python
def lower_bound(cv_results):
    """
    Вычисляет нижнюю границу в пределах 1 стандартного отклонения
    от наилучшего значения `mean_test_scores`.

    Параметры
    ----------
    cv_results : dict of numpy(masked) ndarrays
        См. атрибут cv_results_ `GridSearchCV`

    Возвращает
    -------
    float
        Нижняя граница в пределах 1 стандартного отклонения от наилучшего
        значения `mean_test_score`.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    Балансирует сложность модели с кросс-валидированным показателем качества.

    Параметры
    ----------
    cv_results : dict of numpy(masked) ndarrays
        См. атрибут cv_results_ `GridSearchCV`.

    Возвращает
    -------
    int
        Индекс модели, которая имеет наименьшее количество компонентов PCA,
        при этом ее показатель качества теста находится в пределах 1 стандартного
        отклонения от наилучшего значения `mean_test_score`.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
