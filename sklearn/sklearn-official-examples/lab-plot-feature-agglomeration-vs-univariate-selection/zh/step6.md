# 基于贝叶斯岭回归的单因素方差分析特征选择

```python
f_regression = mem.cache(feature_selection.f_regression)  # 缓存函数
anova = feature_selection.SelectPercentile(f_regression)
clf = Pipeline([("anova", anova), ("ridge", ridge)])
# 通过网格搜索选择最优的特征百分比
clf = GridSearchCV(clf, {"anova__percentile": [5, 10, 20]}, cv=cv)
clf.fit(X, y)  # 设置最佳参数
coef_ = clf.best_estimator_.steps[-1][1].coef_
coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_.reshape(1, -1))
coef_selection_ = coef_.reshape(size, size)
```
