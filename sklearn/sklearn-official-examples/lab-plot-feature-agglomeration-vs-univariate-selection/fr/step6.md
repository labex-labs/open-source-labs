# Sélection de caractéristiques univariée ANOVA suivie de BayesianRidge

```python
f_regression = mem.cache(feature_selection.f_regression)  # fonction de mise en cache
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# Sélectionner le pourcentage optimal de caractéristiques avec une recherche en grille
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # définir les meilleurs paramètres
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
