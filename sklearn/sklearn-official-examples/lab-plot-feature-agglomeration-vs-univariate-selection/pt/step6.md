# Seleção de Recursos Univariada ANOVA seguida de BayesianRidge

```python
f_regression = mem.cache(feature_selection.f_regression)  # armazenando a função
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# Selecionar a porcentagem ideal de recursos com busca em grade
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # definir os melhores parâmetros
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
