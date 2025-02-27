# Настройка модели для обнаружения выбросов

Мы будем использовать `LocalOutlierFactor` для настройки модели для обнаружения выбросов и вычисления предсказанных меток для обучающих образцов.

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
