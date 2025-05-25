# ANOVA 단변량 특징 선택 후 BayesianRidge

```python
f_regression = mem.cache(feature_selection.f_regression)  # 함수 캐싱
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# 그리드 서치를 통해 최적의 특징 비율 선택
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # 최적의 매개변수 설정
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
