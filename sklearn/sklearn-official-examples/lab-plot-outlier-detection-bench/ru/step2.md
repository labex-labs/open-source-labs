# Функция предсказания выбросов

Следующим шагом является определение функции предсказания выбросов. В этом примере мы используем алгоритмы `LocalOutlierFactor` и `IsolationForest`. Функция `compute_prediction` возвращает средний показатель выброса для X.

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Вычисление предсказания для {model_name}...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
