# 非嵌套交叉验证

我们使用非嵌套交叉验证来调整超参数并评估模型的性能。`GridSearchCV` 函数会对估计器的指定参数值进行详尽搜索。我们使用4折交叉验证。

```python
from sklearn.model_selection import GridSearchCV

# 非嵌套参数搜索与评分
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
