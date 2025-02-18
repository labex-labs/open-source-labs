# 非ネスト交差検証（Non-Nested Cross-Validation）

非ネスト交差検証を使用してハイパーパラメータを調整し、モデルの性能を評価します。`GridSearchCV` 関数は、推定器（estimator）の指定されたパラメータ値に対して網羅的な探索を行います。ここでは4分割交差検証を使用します。

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
