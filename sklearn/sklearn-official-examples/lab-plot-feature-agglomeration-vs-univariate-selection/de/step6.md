# Anova-Einfaktor-Feature-Selektion gefolgt von BayesianRidge

```python
f_regression = mem.cache(feature_selection.f_regression)  # Caching-Funktion
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# Wähle den optimalen Feature-Anteil mit Grid Search
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # setze die besten Parameter
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
