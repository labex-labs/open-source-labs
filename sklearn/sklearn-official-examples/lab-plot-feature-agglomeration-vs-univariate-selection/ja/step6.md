# BayesianRidgeに続くAnova単変量特徴選択

```python
f_regression = mem.cache(feature_selection.f_regression)  # キャッシュ関数
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# グリッドサーチにより最適な特徴の割合を選択する
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # 最適なパラメータを設定する
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
