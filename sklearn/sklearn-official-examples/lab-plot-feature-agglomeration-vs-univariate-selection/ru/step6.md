# Выбор признаков с использованием однофакторного дисперсионного анализа (ANOVA), за которым следует BayesianRidge

```python
f_regression = mem.cache(feature_selection.f_regression)  # кэширование функции
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# Выберите оптимальный процент признаков с использованием grid search
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # установите наилучшие параметры
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
